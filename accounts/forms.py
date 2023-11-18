from django.db import models
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm 

class CustomUserCreationForm(UserCreationForm): 
    profile_picture = models.ImageField(upload_to='photos/profile_pictures/', blank=True)
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2','profile_picture']
