from django import forms
from django_countries.data import COUNTRIES
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField




class CheckoutCreateForm(forms.Form):
    billing_name = forms.CharField(label='Full name', required=True, max_length=255)
    email = forms.EmailField(label='Email',required=True, max_length=255)
    shipping_address = forms.CharField(label='Address',required=True, max_length=255)
    postal_code = forms.CharField(label="Zip", required=True, max_length=255)
    country = forms.ChoiceField(choices = sorted(COUNTRIES.items()))
    city = forms.CharField(label='City', max_length=255)


class BillingCreateForm(forms.Form):
    credit_card_name = forms.CharField(label='Credit Card Name', required=True, max_length=255)
    credit_card_number = forms.CharField(label='Credit Card Number',required=True, max_length=16, min_length=16)
    expiration_date = forms.CharField(label='Expiration',required=True, max_length=5)
    cvv = SecurityCodeField(label='CVC',required=True, max_length=3, min_length=3) 






