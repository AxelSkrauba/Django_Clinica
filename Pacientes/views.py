
# Create your views here.

from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from Pacientes.models import Patients, Consultations, Doctors
from .forms import PatientsForm, ConsultationsForm, DoctorsForm

class Index(TemplateView):
    template_name = 'index.html'

class Default(TemplateView):
    template_name = 'default.html'

class Doctor_list(ListView):
    model = Doctors
    template_name = 'doctors.html'
    context_object_name = 'doctors'

class Doctor_new(CreateView):
    model = Doctors
    form_class = DoctorsForm
    template_name = 'doctor_new.html'
    success_url = reverse_lazy('doctor')

class Doctor_edit(UpdateView):
    model = Doctors
    form_class = DoctorsForm
    template_name = 'doctor_edit.html'
    success_url = reverse_lazy('doctor')

class Doctor_delete(DeleteView):
    model = Doctors
    success_url = reverse_lazy('doctor')

class Patient_list(ListView):
    model = Patients
    template_name = 'patients.html'
    context_object_name = 'patients'

class Patient_new(CreateView):
    model = Patients
    form_class = PatientsForm
    template_name = 'patient_new.html'
    success_url = reverse_lazy('patient')

class Patient_edit(UpdateView):
    model = Patients
    form_class = PatientsForm
    template_name = 'patient_edit.html'
    success_url = reverse_lazy('patient')

class Patient_delete(DeleteView):
    model = Patients
    success_url = reverse_lazy('patient')

class Consultation_list(ListView):
    model = Consultations
    template_name = 'consultations.html'
    context_object_name = 'consultations'

class Consultation_new(CreateView):
    model = Consultations
    form_class = ConsultationsForm
    template_name = 'consultation_new.html'
    success_url = reverse_lazy('consultation')

class Consultation_edit(UpdateView):
    model = Consultations
    form_class = ConsultationsForm
    template_name = 'consultation_edit.html'
    success_url = reverse_lazy('consultation')

class Consultation_delete(DeleteView):
    model = Consultations
    success_url = reverse_lazy('consultation')