from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from catalog.models import Item
from user.models import User
from forms.checkout_form import CheckoutCreateForm
from sale.models import Sale
from offer.models import Offer

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
            sale.name = form.cleaned_data.get('billing name')
            sale.buyerid = user
            sale.sellerid = item.sellerid
            sale.itemid = item
            sale.price = item.buyout
            sale.shipping_address = form.cleaned_data.get('address')
            sale.shipped = None
            return redirect('catalog-index')
    else:
        form = CheckoutCreateForm()
    return render(request, 'sale/buyout_item.html', {
        'form': form
    })

def view_buyout_item(request):
    return render(request, 'sale/buyout_item.html')
