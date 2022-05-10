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
            sale = Sale()
            sale.name = form.cleaned_data.get('billing_name')
            sale.buyerid = user
            sale.sellerid = item.sellerid
            sale.itemid = item
            sale.price = item.buyout
            sale.shipping_address = form.cleaned_data.get('address')
            sale.shipped = None
            sale.country = form.cleaned_data.get('country')
            return redirect('catalog-index')
        error_string = '\n'.join([' '.join(l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    else:
        form = CheckoutCreateForm()
    return render(request, 'sale/buyout_item.html', {
        'form': form
    })

def view_buyout_item(request):
    return render(request, 'sale/buyout_item.html')

def view_billing(request):
    return render(request, 'sale/billing_checkout.html')
