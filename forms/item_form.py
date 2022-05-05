from django.forms import ModelForm, widgets
from django import forms
from catalog.models import Item

class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
        exclude = ['sellerid']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'buyout': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }