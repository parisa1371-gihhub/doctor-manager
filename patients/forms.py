from django import forms
from .models import Patient, Visit


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'national_id', 'birth_date', 'gender', 'phone', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'نام را وارد کنید'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'نام خانوادگی را وارد کنید'}),
            'national_id': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'کد ملی را وارد کنید'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'gender': forms.RadioSelect(attrs={'class': 'hidden'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'شماره تلفن را وارد کنید'}),
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'آدرس کامل را وارد کنید'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields required
        for field in self.fields:
            self.fields[field].required = True


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['diagnosis', 'prescription', 'notes', 'next_visit_date']
        widgets = {
            'diagnosis': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'شرح وضعیت، علائم و یافته\u200cهای بیمار'}),
            'prescription': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'لیست داروها، دوزها و دستورات'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'هرگونه مشاهده یا توصیه اضافی'}),
            'next_visit_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make diagnosis required
        self.fields['diagnosis'].required = True
