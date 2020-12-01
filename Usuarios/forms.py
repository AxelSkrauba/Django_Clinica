from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserModuleProfile
from django.contrib.auth.forms import AuthenticationForm


class RegistroForm(UserCreationForm):

    class Meta:
        model = UserModuleProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'rol',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'rol': 'Rol',
        }


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class AsignarRolDoctorForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'}))
	

    class Meta:
        model = UserModuleProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'medic',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'medic': 'Médico Asociado',
        }
