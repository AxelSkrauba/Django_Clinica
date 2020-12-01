from django.urls import path
from Usuarios.views import RegistroUsuario, Login, logoutUsuario


urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name="registrar"),
    path('accounts/login/', Login.as_view(), name="login"),
    path('logout/', logoutUsuario, name="logout"),
]
