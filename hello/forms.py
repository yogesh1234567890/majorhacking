from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hello.models import login

class Form(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =login
        fields=['username','password']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']