from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormularioRegistro(UserCreationForm):
    correo = forms.EmailField(max_length=50, required=True)
    first_name = forms.CharField(label='Primer Nombre',max_length=30, required=True)
    last_name = forms.CharField(label='Primer Apellido', required=True)
    password1 = forms.CharField(label='Contraseña',max_length=10, widget=forms.PasswordInput,required=True)
    password2 = forms.CharField(label='Confirma tu Contraseña',max_length=10, widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields=["username","first_name","last_name","correo", "password1","password2"]