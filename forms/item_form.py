from nis import cat
from django.forms import ModelForm, widgets
from django import forms
from catalog.models import Item
from catalog.models import Category



class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id', 'sellerid', 'offer_accepted']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'label': 'Item name'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'buyout': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.ClearableFileInput(attrs={'class': 'form-control'})
        }
        labels = {
            "name": "Item name",
            "description": "Description",
            "condition": "Condition",
            "buyout": "Buyout Price",
            "image": "Uploaf photo of Item",
            "catid": "Category",
        }