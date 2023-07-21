from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from LoginHandler.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Identificador",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña",max_length=65, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Identificador",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="E-mail",max_length=65,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña",max_length=65, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña",max_length=65, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    hospital_name = forms.CharField(label="Nombre del hospital",max_length=65,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = User
        fields = ['username', 'hospital_name', 'email','password1', 'password2']
        
        