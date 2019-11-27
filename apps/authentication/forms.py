from django.contrib.auth.models import User

#LOGIN
from django.contrib.auth.forms import AuthenticationForm

#REGISTER
from django import forms
from django.contrib.auth.forms import UserCreationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


#REGISTER

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',]
        labels = {
                        'first_name':'Nombres (requerido)',
                        'last_name':'Apellidos (requerido)',
                        'email':'Correo Electronico (requerido)',
                        'username':'Nombre de Usuario (requerido)',
                        'password1':'Contraseña',
                        'password2':'Confirmar Contraseña',
        }
        widgets = {
                           'first_name':forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
                           'last_name':forms.TextInput(attrs={'class':'form-control'}),
                           'email':forms.TextInput(attrs={'class':'form-control'}),
                           'username':forms.TextInput(attrs={'class':'form-control'}),
                           'password1':forms.PasswordInput(attrs={'class':'form-control'}),
                           'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
