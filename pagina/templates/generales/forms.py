from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from pagina.models import MetodoPago

class CustomUserCreationForm(UserCreationForm):
    class Meta():    
        model = get_user_model() 
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']        


class MetodoPagoForm(forms.ModelForm):
    class Meta():
        model = MetodoPago
        fields= '__all__'