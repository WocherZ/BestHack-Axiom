from django.contrib.auth.models import User
from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('balance', )