import re
from django import forms
from django_countries.data import COUNTRIES



class CheckoutCreateForm(forms.Form):
    billing_name = forms.CharField(label='Full name', required=True, max_length=255)
    email = forms.EmailField(label='Email',required=True, max_length=255)
    address = forms.CharField(label='Address',required=True, max_length=255)
    address2 = forms.CharField(label='Address 2',required=False, max_length=255)
    postal_code = forms.CharField(label="Zip", required=True, max_length=255)
    country = forms.ChoiceField(choices = sorted(COUNTRIES.items()))
    city = forms.CharField(label='City', max_length=255)

