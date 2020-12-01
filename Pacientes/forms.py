from datetime import date

from django import forms
from Pacientes.models import Patients, Consultations, Doctors
from django.contrib.admin import widgets


class PatientsForm(forms.ModelForm):

    class Meta:
        model = Patients
        fields = ('first_name', 'last_name', 'dni', 'email',)
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'dni': 'DNI',
            'email': 'Email',
        }


class PatientsMedicForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    dni = forms.CharField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'}))

    class Meta:
        model = Patients
        fields = ('first_name', 'last_name', 'dni', 'email', 'medical_history')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'dni': 'DNI',
            'email': 'Email',
            'medical_history': 'Historial Médico',
        }


class ConsultationsForm(forms.ModelForm):

    today = date.today()
    doctor = forms.Select()
    patient = forms.Select()
    date = forms.DateField(label="Fecha de consulta", widget=forms.SelectDateWidget(
        years=range(today.year, today.year+2)))
    time = forms.TimeField(label="Hora de consulta",
                           help_text="Ejemplo: 8:00", widget=widgets.AdminTimeWidget)

    class Meta:
        model = Consultations
        fields = ('date', 'time', 'doctor', 'patient',)
        labels = {
            'doctor': 'Doctor',
            'patient': 'Paciente',
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(ConsultationsForm, self).clean(*args, **kwargs)
        # Se comprueba que la fecha no pertenezca al pasado
        date = cleaned_data.get('date', None)
        if date is not None:
            if date < self.today:
                self.add_error(
                    'date', 'La consulta no puede especificarse en una fecha "pasada".')

        # Se verifica la disponibilidad del profesional en el horario definido
        doctor = cleaned_data.get('doctor', None)
        time = cleaned_data.get('time', None)
        query = Consultations.objects.all()
        if doctor is not None and time is not None:
            for consultation in query:
                if doctor == consultation.doctor and time == consultation.time and date == consultation.date:
                    self.add_error(
                        'doctor', 'El profesional ya cuenta con un turno asignado en el horario definido.')

        # Si es válida la consulta, se agrega el paciente al doctor.
        patient = cleaned_data.get('patient', None)
        if patient is not None:
            doctor = Doctors.objects.filter(id=doctor.id).first()
            patients = doctor.patients.all()
            patients_id = []
            for p_id in patients:
                patients_id.append(p_id.pk)
            patients_id.append(patient.pk)
            doctor.patients.set(patients_id)


class ConsultationsMedicForm(forms.ModelForm):
    patient = forms.Select(attrs={'readonly': 'readonly'})
    date = forms.DateField(label="Fecha de consulta", widget=forms.SelectDateWidget(
        attrs={'readonly': 'readonly'}))
    time = forms.TimeField(label="Hora de consulta",
                           widget=widgets.AdminTimeWidget(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Consultations
        fields = ('date', 'time', 'patient', 'attended',)
        labels = {
            'patient': 'Paciente',
            'attended': 'Se atendió',
        }
    

class DoctorsForm(forms.ModelForm):

    class Meta:
        model = Doctors
        fields = ('first_name', 'last_name',)
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
