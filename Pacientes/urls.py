from django.urls import path
from django.contrib.auth.decorators import login_required
from Pacientes import views

urlpatterns = [
    path('', login_required(views.Index.as_view()), name="index"),
    path('default/', views.Default.as_view(), name="default"),
    path('doctor/', login_required(views.Doctor_list.as_view()), name="doctor"),
    path('doctor/new/', login_required(views.Doctor_new.as_view()), name="doctor_new"),
    path('doctor/<int:pk>', login_required(views.Doctor_edit.as_view()), name="doctor_edit"),
    path('doctor/delete/<int:pk>', login_required(views.Doctor_delete.as_view()), name="doctor_delete"),
    path('patient/', login_required(views.Patient_list.as_view()), name="patient"),
    path('patient/new/', login_required(views.Patient_new.as_view()), name="patient_new"),
    path('patient/<int:pk>', login_required(views.Patient_edit.as_view()), name="patient_edit"),
    path('patient/delete/<int:pk>', login_required(views.Patient_delete.as_view()), name="patient_delete"),
    path('consultation/', login_required(views.Consultation_list.as_view()), name="consultation"),
    path('consultation/new/', login_required(views.Consultation_new.as_view()), name="consultation_new"),
    path('consultation/<int:pk>', login_required(views.Consultation_edit.as_view()), name="consultation_edit"),
    path('consultation/delete/<int:pk>', login_required(views.Consultation_delete.as_view()), name="consultation_delete"),
]