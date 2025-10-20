from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Patient, Visit
from .forms import PatientForm, VisitForm


def dashboard(request):
    """Dashboard view with statistics and recent activity"""
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