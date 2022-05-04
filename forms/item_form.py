from django.forms import ModelForm, widgets
from django import forms
from catalog.models import Item

class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),)
    class Meta:
        model = Item
        exclude = ['id']
        exclude = ['sellerid']
        widgets = {
            'Item Name': widgets.TextInput(attrs={'class': 'form-control'}),
            'Condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'Description': widgets.Select(attrs={'class': 'form-control'}),
            'Ships To': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Pick Up Available': widgets.Select(attrs={'class': 'form-control'}),
        }