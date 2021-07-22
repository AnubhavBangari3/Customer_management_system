from django import forms
from django.forms import ModelForm
from .models import Order

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=120)
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model=User
        fields=('username','email','password1','password2',)