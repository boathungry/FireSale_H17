from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Item
from user.models import User
from sale.models import Sale
from forms.checkout_form import CheckoutCreateForm, BillingCreateForm
from django.contrib import messages
import datetime
# Create your views here.


@login_required
def create_checkout(request, id):
    """Create the checkout address/name/etc. form and move on to billing once it's been submitted"""
    if request.method == 'POST':
        form = CheckoutCreateForm(data=request.POST)
        if form.is_valid() :#and request.POST.get('step') == 'shipping':
            request.session['billing_name'] = form.cleaned_data.get('billing_name')
            request.session['email'] = form.cleaned_data.get('email')
            request.session['shipping_address'] = form.cleaned_data.get('shipping_address')
            request.session['postal_code'] = form.cleaned_data.get('postal_code')
            request.session['country'] = form.cleaned_data.get('country')
            request.session['city'] = form.cleaned_data.get('city')
            return redirect('billing_checkout', id=id)
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
        'form': form,
        'item': Item.objects.get(pk=id)
    })

@login_required
def create_billing(request, id):
    """Create the checkout billing form and move on to overview once it's been submitted"""
    if request.method == 'POST':
        form = BillingCreateForm(data=request.POST)
        if form.is_valid():
            request.session['credit_card_name'] = form.cleaned_data.get('credit_card_name')
            request.session['credit_card_number'] = form.cleaned_data.get('credit_card_number')
            request.session['expiration_date'] = form.cleaned_data.get('expiration_date')
            request.session['cvv'] = form.cleaned_data.get('cvv')
            return redirect('checkout_overview', id=id)
        error_string = '\n'.join([' '.join(l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    else:
        form = BillingCreateForm()
        if 'credit_card_name' in request.session:
            form.fields['credit_card_name'].initial = request.session['credit_card_name']
            form.fields['credit_card_number'].initial = request.session['credit_card_number']
            form.fields['expiration_date'].initial = request.session['expiration_date']
            form.fields['cvv'].initial = request.session['cvv']
    return render(request, 'sale/billing_checkout.html', {
        'form': form,
        'item': Item.objects.get(pk=id)
    })


@login_required
def view_checkout_overview(request, id):
    """Get an overview of the order"""
    if request.method == 'GET':
        context = {
            'item': Item.objects.get(pk=id),
            'billing_name': request.session["billing_name"],
            'email': request.session["email"],
            'shipping_address': request.session["shipping_address"],
            'postal_code': request.session["postal_code"],
            'country': request.session["country"],
            'city': request.session["city"],}
    return render(request, 'sale/checkout_overview.html', context)


@login_required
def checkout_final(request, id):
    """Finish checking out"""
    if 'shipping_address' in request.session and 'credit_card_number' in request.session:
        context = {'item': Item.objects.get(id=id)}
        authuser = request.user
        user = User.objects.get(id=authuser.id)
        item = Item.objects.get(id=id)
        sale = Sale()
        sale.itemid = item
        sale.buyerid = user
        sale.sellerid = item.sellerid
        sale.price = item.buyout
        sale.shipped = datetime.datetime.now() 
        sale.shipping_address = request.session['shipping_address']
        sale.postal_code = request.session['postal_code']
        sale.country = request.session['country']
        sale.city = request.session['city']
        sale.save()
        item.offer_accepted = True
        item.save()
        request.session.clear()
        return render(request, "sale/checkout_confirmation.html", context)