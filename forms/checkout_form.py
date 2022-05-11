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
    credit_card_number = CardNumberField(label='Credit Card Number',required=True, min_length=16)
    expiration_date = CardExpiryField(label='Expiration',required=True)
    cvv = SecurityCodeField(label='CVV',required=False, max_length=255) 






