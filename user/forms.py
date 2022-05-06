from django import forms
from .models import User


class AccountCreationForm(forms.Form):
    name = forms.CharField(label='Full name', required=True, max_length=255)
    bio = forms.CharField(label='Bio', max_length=510)
    image = forms.CharField(label='Profile picture (link)', max_length=999)