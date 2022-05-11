import re
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from catalog.models import Item
from user.models import User
from forms.checkout_form import CheckoutCreateForm
from sale.models import Sale
from django.contrib import messages
# Create your views here.


@login_required
def create_checkout(request, id):
    if request.method == 'POST':
        form = CheckoutCreateForm(data=request.POST)
        authuser = request.user
        user = User.objects.get(auth=authuser.id)
        item = Item.objects.get(id=id)
        if form.is_valid():
            request.session['billing_name'] = form.cleaned_data.get('billing_name')
            request.session['email'] = form.cleaned_data.get('email')
            request.session['shipping_address'] = form.cleaned_data.get('shipping_address')
            request.session['postal_code'] = form.cleaned_data.get('postal_code')
            request.session['country'] = form.cleaned_data.get('country')
            request.session['city'] = form.cleaned_data.get('city')
            return redirect('catalog-index')
        error_string = '\n'.join([' '.join(l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    else:
        form = CheckoutCreateForm()
        if 'billing_name' in request.session:
            form.fields['billing_name'].initial = request.session['billing_name']
            form.fields['email'].initial = request.session['email']
            form.fields['shipping_address'].initial = request.session['shipping_address']
            form.fields['postal_code'].initial = request.session['postal_code']
            form.fields['country'].initial = request.session['country']
            form.fields['city'].initial = request.session['city']
    return render(request, 'sale/buyout_item.html', {
        'form': form
    })

@login_required
def create_billing(request, id):
    if request.method == 'POST':
        form = CheckoutCreateForm(data=request.POST)
        authuser = request.user
        user = User.objects.get(auth=authuser.id)
        item = Item.objects.get(id=id)
        if form.is_valid():
            request.session['credit_card_name'] = form.cleaned_data.get('credit_card_name')
            request.session['credit_card_number'] = form.cleaned_data.get('credit_card_number')
            request.session['expiration_date'] = form.cleaned_data.get('expiration_date')
            request.session['cvv'] = form.cleaned_data.get('cvv')
            return redirect('catalog-index')
        error_string = '\n'.join([' '.join(l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    else:
        form = CheckoutCreateForm()
        if 'credit_card_name' in request.session:
            form.fields['credit_card_name'].initial = request.session['credit_card_name']
            form.fields['credit_card_number'].initial = request.session['credit_card_number']
            form.fields['expiration_date'].initial = request.session['expiration_date']
            form.fields['cvv'].initial = request.session['cvv']
    return render(request, 'sale/buyout_item.html', {
        'form': form
    })


def view_buyout_item(request):
    return render(request, 'sale/buyout_item.html')

def view_billing(request):
    return render(request, 'sale/billing_checkout.html')

def view_checkout_steps(request):
    return render(request, 'sale/checkout_steps.html')
