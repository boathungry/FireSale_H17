from django.forms import ModelForm, widgets
from django import forms
from offer.models import Offer

class CheckoutCreateForm(ModelForm):
    class Meta:
        model = Offer
        widgets = {
            'billing name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'address 2': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.Select(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'})
        }