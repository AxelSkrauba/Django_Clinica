from django.urls import path
from Pacientes import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('default/', views.Default.as_view(), name="default"),
    path('doctor/', views.Doctor_list.as_view(), name="doctor"),
    path('doctor/new/', views.Doctor_new.as_view(), name="doctor_new"),
    path('doctor/<int:pk>', views.Doctor_edit.as_view(), name="doctor_edit"),
    path('doctor/delete/<int:pk>', views.Doctor_delete.as_view(), name="doctor_delete"),
    path('patient/', views.Patient_list.as_view(), name="patient"),
    path('patient/new/', views.Patient_new.as_view(), name="patient_new"),
    path('patient/<int:pk>', views.Patient_edit.as_view(), name="patient_edit"),
    path('patient/delete/<int:pk>', views.Patient_delete.as_view(), name="patient_delete"),
    path('consultation/', views.Consultation_list.as_view(), name="consultation"),
    path('consultation/new/', views.Consultation_new.as_view(), name="consultation_new"),
    path('consultation/<int:pk>', views.Consultation_edit.as_view(), name="consultation_edit"),
    path('consultation/delete/<int:pk>', views.Consultation_delete.as_view(), name="consultation_delete"),
]