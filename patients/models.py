from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


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
    birth_date = models.DateField()
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
        from datetime import date
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    prescription = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    next_visit_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-visit_date']
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.visit_date.strftime('%Y-%m-%d')}"