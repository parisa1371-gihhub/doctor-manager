from django.contrib import admin
from .models import Patient, Visit


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'national_id', 'phone', 'age', 'gender', 'created_at']
    list_filter = ['gender', 'created_at']
    search_fields = ['first_name', 'last_name', 'national_id', 'phone']
    ordering = ['last_name', 'first_name']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'national_id', 'birth_date', 'gender')
        }),
        ('Contact Information', {
            'fields': ('phone', 'address')
        }),
    )


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['patient', 'visit_date', 'diagnosis_short', 'next_visit_date']
    list_filter = ['visit_date', 'patient']
    search_fields = ['patient__first_name', 'patient__last_name', 'diagnosis']
    ordering = ['-visit_date']
    
    def diagnosis_short(self, obj):
        return obj.diagnosis[:50] + '...' if len(obj.diagnosis) > 50 else obj.diagnosis
    diagnosis_short.short_description = 'Diagnosis'
    
    fieldsets = (
        ('Visit Information', {
            'fields': ('patient', 'visit_date')
        }),
        ('Medical Information', {
            'fields': ('diagnosis', 'prescription', 'notes')
        }),
        ('Follow-up', {
            'fields': ('next_visit_date',)
        }),
    )