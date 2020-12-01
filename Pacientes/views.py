
# Create your views here.

from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from Pacientes.models import Patients, Consultations, Doctors
from Usuarios.models import UserModuleProfile
from Usuarios.forms import AsignarRolDoctorForm
from .forms import PatientsForm, ConsultationsForm, DoctorsForm, PatientsMedicForm, ConsultationsMedicForm



from datetime import date


class Index(TemplateView):
    template_name = 'Pacientes/index.html'


class Default(TemplateView):
    template_name = 'Pacientes/default.html'


class Doctor_list(ListView):
    model = Doctors
    template_name = 'Pacientes/doctors.html'
    context_object_name = 'doctors'

class Doctor_Gerency_list(ListView):
    model = UserModuleProfile
    template_name = 'Pacientes/doctors_gerency.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        """
        Se buscan los usuarios con el rol de médicos
        """
        doctors = Doctors.objects.all()
        id_doctors = []
        for doctor in doctors:
            id_doctors.append(doctor.id)
        queryset = UserModuleProfile.objects.filter(medic_id__in=id_doctors)
        return queryset



class Doctor_new(CreateView):
    model = Doctors
    form_class = DoctorsForm
    template_name = 'Pacientes/doctor_new.html'
    success_url = reverse_lazy('doctor')



class Doctor_Gerency_edit(UpdateView):
    model = UserModuleProfile
    form_class = AsignarRolDoctorForm
    template_name = 'Pacientes/doctor_edit.html'
    success_url = reverse_lazy('doctor')



class Doctor_edit(UpdateView):
    model = Doctors
    form_class = DoctorsForm
    template_name = 'Pacientes/doctor_edit.html'
    success_url = reverse_lazy('doctor')


class Doctor_delete(DeleteView):
    model = Doctors
    success_url = reverse_lazy('doctor')


class Patient_list(ListView):
    model = Patients
    template_name = 'Pacientes/patients.html'
    context_object_name = 'patients'


class Patient_Medic_list(ListView):
    model = Patients
    template_name = 'Pacientes/patients.html'
    context_object_name = 'patients'

    def get_queryset(self):
        """
        Se buscan los pacientes asociados al doctor en sesión
        La queryset se establece en base a las coicidencias
        """
        user_id = self.request.user.pk
        users = UserModuleProfile.objects.all()
        id_medic = 0
        for user in users:
            if user.id == user_id:
                id_medic = user.medic.id
        medics = Doctors.objects.filter(id=id_medic)
        patients = []
        for doc in medics:
            for patient in doc.patients.all():
                patients.append(patient.id)
            queryset = Patients.objects.filter(id__in=patients)
        return queryset


class Patient_new(CreateView):
    model = Patients
    form_class = PatientsForm
    template_name = 'Pacientes/patient_new.html'
    success_url = reverse_lazy('patient')


class Patient_edit(UpdateView):
    model = Patients
    form_class = PatientsForm
    template_name = 'Pacientes/patient_edit.html'
    success_url = reverse_lazy('patient')


class Patient_Medic_edit(UpdateView):
    model = Patients
    form_class = PatientsMedicForm
    template_name = 'Pacientes/patient_edit.html'
    success_url = reverse_lazy('patient')


class Patient_delete(DeleteView):
    model = Patients
    success_url = reverse_lazy('patient')


class Consultation_list(ListView):
    model = Consultations
    template_name = 'Pacientes/consultations.html'
    context_object_name = 'consultations'
    

class Consultation_Medic_list(ListView):
    model = Consultations
    template_name = 'Pacientes/consultations.html'
    context_object_name = 'consultations'

    def get_queryset(self):
        """
        Se buscan los pacientes asociados al doctor en sesión
        La queryset se establece en base a las coicidencias
        """
        user_id = self.request.user.pk
        users = UserModuleProfile.objects.all()
        id_medic = 0
        for user in users:
            if user.id == user_id:
                id_medic = user.medic.id
        queryset = Consultations.objects.filter(doctor=id_medic)
        return queryset


class Consultation_new(CreateView):
    model = Consultations
    form_class = ConsultationsForm
    template_name = 'Pacientes/consultation_new.html'
    success_url = reverse_lazy('consultation')


class Consultation_edit(UpdateView):
    model = Consultations
    form_class = ConsultationsForm
    template_name = 'Pacientes/consultation_edit.html'
    success_url = reverse_lazy('consultation')


class Consultation_Medic_edit(UpdateView):
    model = Consultations
    form_class = ConsultationsMedicForm
    template_name = 'Pacientes/consultation_edit.html'
    success_url = reverse_lazy('consultation')


class Consultation_delete(DeleteView):
    model = Consultations
    success_url = reverse_lazy('consultation')
