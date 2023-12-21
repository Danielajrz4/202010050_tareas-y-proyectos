from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta():    
        model = get_user_model() 
        fields = ['username', 'email', 'first_name', 'last_name','NumCel','DPI', 'password1', 'password2']        