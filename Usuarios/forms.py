from django.contrib.auth.forms import UserCreationForm
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
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'