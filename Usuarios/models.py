from django.contrib.auth.models import User
from django.db import models


ROL = [
    ('SEC', "Secretaría"),
    ('DOC', "Doctor"),
    ('VEN', "Ventas"),
    ('TAL', "Taller"),
    ('GER', "Gerencia"),
]


class UserModuleProfile(User):
    rol = models.CharField(max_length=3, choices=ROL)
    