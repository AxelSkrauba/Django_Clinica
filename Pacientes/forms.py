from django import forms
from Pacientes.models import Patients, Consultations, Doctors

class PatientsForm(forms.ModelForm):

    class Meta:
        model = Patients
        fields = ('first_name', 'last_name', 'dni', 'email',)
       
class ConsultationsForm(forms.ModelForm):
    doctor = forms.Select()
    patient = forms.Select()
    date = forms.Select()

    class Meta:
        model = Consultations
        fields = ('date', 'time', 'doctor', 'patient',)

class DoctorsForm(forms.ModelForm):
    patients = forms.Select()
    
    class Meta:
        model = Doctors
        fields = ('first_name', 'last_name', 'patients',)
