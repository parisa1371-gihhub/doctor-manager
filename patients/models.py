from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import date


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'مرد'),
        ('F', 'زن'),
        ('O', 'سایر'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(
            regex=r'^\d+$',
            message='کد ملی باید فقط شامل اعداد باشد'
        )]
    )
    birth_date = models.CharField(max_length=10, help_text="تاریخ تولد به صورت شمسی (YYYY/MM/DD)")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message='شماره تلفن باید در فرمت صحیح وارد شود. حداکثر 15 رقم مجاز است.'
        )]
    )
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        if not self.birth_date:
            return None
        
        try:
            # Parse Jalali date (YYYY/MM/DD)
            parts = self.birth_date.split('/')
            if len(parts) != 3:
                return None
                
            jalali_year = int(parts[0])
            
            # Simple age calculation from Jalali year (approximate)
            current_jalali_year = 1403  # Current Jalali year
            return current_jalali_year - jalali_year
                
        except (ValueError, IndexError):
            return None


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    prescription = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    next_visit_date = models.CharField(max_length=10, null=True, blank=True, help_text="تاریخ ویزیت بعدی به صورت شمسی (YYYY/MM/DD)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-visit_date']
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.visit_date.strftime('%Y-%m-%d')}"