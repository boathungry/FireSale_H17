from django.forms import ModelForm, widgets
from django import forms
from catalog.models import Item
from catalog.models import Category

categories = list(Category.objects.values())

class ItemCreateForm(forms.Form):
    name = forms.CharField(label='Item name', required=True, max_length=255)
    description = forms.CharField(label='Description', required=False, max_length=255)
    condition = forms.CharField(label='Condition', max_length=255)
    buyout = forms.FloatField(label='Buyout Price')
    catid = forms.ChoiceField(label='Category', choices=categories)
    image = forms.ImageField(label='Photo of item')



    class Meta:
        model = Item
