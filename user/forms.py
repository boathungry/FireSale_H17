from django import forms
from .models import User


class AccountCreationForm(forms.Form):
    name = forms.CharField(label='Full name', required=True, max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    bio = forms.CharField(label='Bio', max_length=510)
    image = forms.ImageField(label='Profile picture (link)', max_length=999)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'bio', 'image']