from django.contrib.auth.models import User
from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    balance = forms.CharField(label='Введите сумму пополнения', widget=forms.TextInput(attrs={'placeholder': 'Сумма пополнения'}))
    class Meta:
        model = Profile
        fields = ('balance', )