from django.contrib.auth.models import User
from django.db import models
from Pacientes.models import Doctors


ROL = [
    ('SEC', "Secretaría"),
    ('DOC', "Doctor"),
    ('VEN', "Ventas"),
    ('TAL', "Taller"),
    ('GER', "Gerencia"),
]
#Roles pensados para añadir los usuarios los grupos con sus permisos, automáticamente
#Por el momento, no implementado

class UserModuleProfile(User):
    rol = models.CharField(max_length=3, choices=ROL)
    medic = models.OneToOneField(Doctors, default=None, null=True, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)