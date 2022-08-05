from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario

class FormCreacionUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',

        )

class FormCreacionPerfil(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ('genero',  )

"""class FormIniciarSesion(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormIniciarSesion,self).__init__(*args, **kwargs)
        agregar"""


