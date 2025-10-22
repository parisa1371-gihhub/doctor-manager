from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Patient, Visit, Notification
from .forms import PatientForm, VisitForm


def dashboard(request):
    """Dashboard view with statistics and recent activity"""
    # Create appointment notifications for upcoming appointments
    create_appointment_notifications()
    
    # Get statistics
    total_patients = Patient.objects.count()
    
    # Get today's visits
    today = timezone.now().date()
    today_visits = Visit.objects.filter(visit_date__date=today).count()
    
    # Get this week's visits
    week_start = today - timedelta(days=today.weekday())
    week_visits = Visit.objects.filter(visit_date__date__gte=week_start).count()
    
    # Get this month's visits
    month_start = today.replace(day=1)
    month_visits = Visit.objects.filter(visit_date__date__gte=month_start).count()
    
    # Get recent visits (last 5)
    recent_visits = Visit.objects.select_related('patient').order_by('-visit_date')[:5]
    
    # Get recent patients (last 10)
    recent_patients = Patient.objects.prefetch_related('visits').order_by('-created_at')[:10]
    
    context = {
        'total_patients': total_patients,
        'today_visits': today_visits,
        'week_visits': week_visits,
        'month_visits': month_visits,
        'recent_visits': recent_visits,
        'recent_patients': recent_patients,
    }
    
    return render(request, 'dashboard.html', context)


def patients_list(request):
    """List all patients with search functionality"""
    patients = Patient.objects.prefetch_related('visits').order_by('last_name', 'first_name')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        patients = patients.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(national_id__icontains=search_query) |
            Q(phone__icontains=search_query)
        )
    
    context = {
        'patients': patients,
        'search_query': search_query,
    }
    
    return render(request, 'patients.html', context)


def add_patient(request):
    """Add a new patient"""
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'بیمار {patient.full_name} با موفقیت اضافه شد!')
            return redirect('patient_detail', patient_id=patient.id)
    else:
        form = PatientForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'add_patient.html', context)


def patient_detail(request, patient_id):
    """View patient details and medical history"""
    patient = get_object_or_404(Patient, id=patient_id)
    
    context = {
        'patient': patient,
    }
    
    return render(request, 'patient_detail.html', context)


def edit_patient(request, patient_id):
    """Edit patient information"""
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, f'اطلاعات بیمار {patient.full_name} با موفقیت به‌روزرسانی شد!')
            return redirect('patient_detail', patient_id=patient.id)
    else:
        form = PatientForm(instance=patient)
    
    context = {
        'form': form,
        'patient': patient,
    }
    
    return render(request, 'edit_patient.html', context)


def add_visit(request, patient_id):
    """Add a new visit for a patient"""
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.patient = patient
            visit.save()
            messages.success(request, f'سابقه ویزیت برای {patient.full_name} اضافه شد!')
            return redirect('patient_detail', patient_id=patient.id)
    else:
        form = VisitForm()
    
    context = {
        'form': form,
        'patient': patient,
    }
    
    return render(request, 'add_visit.html', context)


def appointments_list(request):
    """List all appointments (visits with next_visit_date)"""
    # Get all visits that have a next visit date
    appointments = Visit.objects.filter(
        next_visit_date__isnull=False
    ).exclude(
        next_visit_date=''
    ).select_related('patient').order_by('next_visit_date')
    
    # Count total appointments
    total_appointments = appointments.count()
    
    # Get upcoming appointments (next 7 days)
    from datetime import datetime, timedelta
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    
    # Convert Jalali dates to Gregorian for comparison
    upcoming_appointments = []
    for appointment in appointments:
        try:
            # Parse Jalali date
            jalali_parts = appointment.next_visit_date.split('/')
            if len(jalali_parts) == 3:
                jalali_year = int(jalali_parts[0])
                jalali_month = int(jalali_parts[1])
                jalali_day = int(jalali_parts[2])
                
                # Convert to Gregorian using jdatetime
                try:
                    import jdatetime
                    jalali_date = jdatetime.date(jalali_year, jalali_month, jalali_day)
                    gregorian_date = jalali_date.togregorian()
                except:
                    # Fallback: simple approximation
                    gregorian_date = today
                
                if today <= gregorian_date <= next_week:
                    upcoming_appointments.append({
                        'visit': appointment,
                        'gregorian_date': gregorian_date
                    })
        except:
            continue
    
    context = {
        'appointments': appointments,
        'total_appointments': total_appointments,
        'upcoming_appointments': upcoming_appointments,
    }
    
    return render(request, 'appointments.html', context)


def notifications_list(request):
    """Display all notifications"""
    notifications = Notification.objects.all().order_by('-created_at')
    unread_count = Notification.objects.filter(is_read=False).count()
    
    context = {
        'notifications': notifications,
        'unread_count': unread_count,
    }
    
    return render(request, 'notifications.html', context)


def mark_notification_read(request, notification_id):
    """Mark a notification as read"""
    notification = get_object_or_404(Notification, id=notification_id)
    notification.is_read = True
    notification.save()
    
    return redirect('notifications')


def create_appointment_notifications():
    """Create notifications for upcoming appointments (next 7 days)"""
    from datetime import datetime, timedelta
    import jdatetime
    
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    
    # Clean up orphaned notifications (notifications for deleted patients)
    orphaned_notifications = Notification.objects.filter(
        related_patient__isnull=True
    )
    if orphaned_notifications.exists():
        orphaned_notifications.delete()
    
    # Get visits with next_visit_date in the next 7 days
    visits = Visit.objects.filter(
        next_visit_date__isnull=False
    ).exclude(
        next_visit_date=''
    ).select_related('patient')
    
    for visit in visits:
        try:
            # Parse Jalali date
            jalali_parts = visit.next_visit_date.split('/')
            if len(jalali_parts) == 3:
                jalali_year = int(jalali_parts[0])
                jalali_month = int(jalali_parts[1])
                jalali_day = int(jalali_parts[2])
                
                # Convert to Gregorian
                jalali_date = jdatetime.date(jalali_year, jalali_month, jalali_day)
                gregorian_date = jalali_date.togregorian()
                
                # Create notification for appointments in the next 7 days
                if today <= gregorian_date <= next_week:
                    # Check if notification already exists for this visit
                    existing_notification = Notification.objects.filter(
                        related_visit=visit,
                        notification_type='appointment',
                        is_read=False
                    ).first()
                    
                    if not existing_notification:
                        # Calculate days until appointment
                        days_until = (gregorian_date - today).days
                        
                        if days_until == 0:
                            title = f"قرار ملاقات امروز - {visit.patient.full_name}"
                            message = f"قرار ملاقات با {visit.patient.full_name} امروز است."
                        elif days_until == 1:
                            title = f"قرار ملاقات فردا - {visit.patient.full_name}"
                            message = f"قرار ملاقات با {visit.patient.full_name} فردا است."
                        elif days_until <= 3:
                            title = f"قرار ملاقات نزدیک - {visit.patient.full_name}"
                            message = f"قرار ملاقات با {visit.patient.full_name} در {days_until} روز آینده ({visit.next_visit_date}) است."
                        else:
                            title = f"قرار ملاقات هفته آینده - {visit.patient.full_name}"
                            message = f"قرار ملاقات با {visit.patient.full_name} در {days_until} روز آینده ({visit.next_visit_date}) است."
                        
                        Notification.objects.create(
                            title=title,
                            message=message,
                            notification_type='appointment',
                            related_patient=visit.patient,
                            related_visit=visit
                        )
        except Exception as e:
            # Log error but continue processing
            continue


def create_appointment_notifications_manual(request):
    """Manually create appointment notifications"""
    try:
        create_appointment_notifications()
        messages.success(request, 'اعلان‌های قرار ملاقات با موفقیت ایجاد شدند.')
    except Exception as e:
        messages.error(request, f'خطا در ایجاد اعلان‌ها: {str(e)}')
    
    return redirect('dashboard')


def settings_page(request):
    """Settings page for system configuration"""
    if request.method == 'POST':
        # Handle settings form submission
        action = request.POST.get('action')
        
        if action == 'change_language':
            language = request.POST.get('language')
            if language in ['fa', 'en']:
                # Store language preference in session
                request.session['language'] = language
                messages.success(request, f'زبان سیستم به {language} تغییر یافت.')
            else:
                messages.error(request, 'زبان انتخابی معتبر نیست.')
        
        elif action == 'toggle_notifications':
            notifications_enabled = request.POST.get('notifications_enabled') == 'on'
            request.session['notifications_enabled'] = notifications_enabled
            status = 'فعال' if notifications_enabled else 'غیرفعال'
            messages.success(request, f'اعلان‌ها {status} شدند.')
        
        elif action == 'change_theme':
            theme = request.POST.get('theme')
            if theme in ['light', 'dark', 'auto']:
                request.session['theme'] = theme
                messages.success(request, f'تم سیستم به {theme} تغییر یافت.')
            else:
                messages.error(request, 'تم انتخابی معتبر نیست.')
        
        elif action == 'update_profile':
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            email = request.POST.get('email', '').strip()
            
            # Validation
            if not first_name or not last_name:
                messages.error(request, 'نام و نام خانوادگی الزامی است.')
            elif not email or '@' not in email:
                messages.error(request, 'ایمیل معتبر وارد کنید.')
            else:
                try:
                    # Check if email is already used by another user
                    if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                        messages.error(request, 'این ایمیل قبلاً توسط کاربر دیگری استفاده شده است.')
                    else:
                        # Update user profile
                        request.user.first_name = first_name
                        request.user.last_name = last_name
                        request.user.email = email
                        request.user.save()
                        
                        messages.success(request, f'پروفایل شما با موفقیت به‌روزرسانی شد! خوش آمدید، دکتر {first_name} {last_name}')
                except Exception as e:
                    messages.error(request, f'خطا در به‌روزرسانی پروفایل: {str(e)}')
        
        return redirect('settings')
    
    # Get current settings from session
    current_language = request.session.get('language', 'fa')
    notifications_enabled = request.session.get('notifications_enabled', True)
    current_theme = request.session.get('theme', 'light')
    
    context = {
        'user': request.user,
        'current_language': current_language,
        'notifications_enabled': notifications_enabled,
        'current_theme': current_theme,
        'django_version': '5.1.7',
        'system_startup_date': datetime.now(),
    }
    return render(request, 'settings.html', context)


def login_view(request):
    """Login page for doctor"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if first_name and username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Update user's first name if provided
                if first_name and first_name != user.first_name:
                    user.first_name = first_name
                    user.save()
                
                login(request, user)
                messages.success(request, f'خوش آمدید، دکتر {user.get_full_name() or user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
        else:
            messages.error(request, 'لطفاً همه فیلدها را پر کنید.')
    
    return render(request, 'login.html')


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'با موفقیت از سیستم خارج شدید.')
    return redirect('login')

