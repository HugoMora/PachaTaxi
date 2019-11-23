from django.contrib.auth.forms import AuthenticationForm
from django import forms


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class RegisterForm(forms.Form):
    
    first_name = forms.CharField(required = True, min_length=4, max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Nombres'}))
