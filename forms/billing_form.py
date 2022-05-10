from django import forms
from django_countries.data import COUNTRIES



class CheckoutCreateForm(forms.Form):
    credit_card_name = forms.CharField(label='Credit Card Name', required=True, max_length=255)
    credit_card_number = forms.EmailField(label='Credit Card Number',required=True, max_length=255)
    expiration_date = forms.CharField(label='Expiration',required=True, max_length=255)
    cvv = forms.CharField(label='CVV',required=False, max_length=255)


