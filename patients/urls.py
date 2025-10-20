from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patients/', views.patients_list, name='patients'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:patient_id>/edit/', views.edit_patient, name='edit_patient'),
    path('patients/<int:patient_id>/visit/', views.add_visit, name='add_visit'),
    path('appointments/', views.appointments_list, name='appointments'),
    path('notifications/', views.notifications_list, name='notifications'),
    path('notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
]

