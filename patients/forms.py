from django import forms
from .models import Patient, Visit
import re


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'national_id', 'birth_date', 'gender', 'phone', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'نام را وارد کنید'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'نام خانوادگی را وارد کنید'}),
            'national_id': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'کد ملی را وارد کنید'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'تاریخ تولد (شمسی)'}),
            'gender': forms.RadioSelect(attrs={'class': 'hidden'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'شماره تلفن را وارد کنید'}),
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'آدرس کامل را وارد کنید'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields required
        for field in self.fields:
            self.fields[field].required = True
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date:
            # Validate Jalali date format (YYYY/MM/DD)
            if not re.match(r'^\d{4}/\d{2}/\d{2}$', birth_date):
                raise forms.ValidationError('فرمت تاریخ صحیح نیست. لطفاً تاریخ را به صورت YYYY/MM/DD وارد کنید.')
            
            # Validate date components
            try:
                parts = birth_date.split('/')
                year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
                
                # Basic validation for Jalali dates
                if not (1300 <= year <= 1500):
                    raise forms.ValidationError('سال باید بین 1300 تا 1500 باشد.')
                if not (1 <= month <= 12):
                    raise forms.ValidationError('ماه باید بین 1 تا 12 باشد.')
                if not (1 <= day <= 31):
                    raise forms.ValidationError('روز باید بین 1 تا 31 باشد.')
                    
            except ValueError:
                raise forms.ValidationError('فرمت تاریخ صحیح نیست.')
                
        return birth_date


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['diagnosis', 'prescription', 'notes', 'next_visit_date']
        widgets = {
            'diagnosis': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'شرح وضعیت، علائم و یافته\u200cهای بیمار'}),
            'prescription': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'لیست داروها، دوزها و دستورات'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'هرگونه مشاهده یا توصیه اضافی'}),
            'next_visit_date': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'تاریخ ویزیت بعدی (شمسی)'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make diagnosis required
        self.fields['diagnosis'].required = True
    
    def clean_next_visit_date(self):
        next_visit_date = self.cleaned_data.get('next_visit_date')
        if next_visit_date:
            # Validate Jalali date format (YYYY/MM/DD)
            if not re.match(r'^\d{4}/\d{2}/\d{2}$', next_visit_date):
                raise forms.ValidationError('فرمت تاریخ صحیح نیست. لطفاً تاریخ را به صورت YYYY/MM/DD وارد کنید.')
            
            # Validate date components
            try:
                parts = next_visit_date.split('/')
                year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
                
                # Basic validation for Jalali dates
                if not (1300 <= year <= 1500):
                    raise forms.ValidationError('سال باید بین 1300 تا 1500 باشد.')
                if not (1 <= month <= 12):
                    raise forms.ValidationError('ماه باید بین 1 تا 12 باشد.')
                if not (1 <= day <= 31):
                    raise forms.ValidationError('روز باید بین 1 تا 31 باشد.')
                    
            except ValueError:
                raise forms.ValidationError('فرمت تاریخ صحیح نیست.')
                
        return next_visit_date
