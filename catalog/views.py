from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Category, Item
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from offer.models import Offer
from user.models import User
from django.http import JsonResponse
from django.db.models import Max

# Create your views here.
from forms.item_form import ItemCreateForm


def index(request):
    order_by_values = {
        "high": "-buyout",
        "low": "buyout",
        "name": "name",
        "new": "-id",
    }
    order_option = request.GET.get("order-by", 'name')

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        order_option = request.GET.get("order-by", "name")
        items = list(Item.objects.filter(name__icontains=search_filter).values().order_by(order_by_values[order_option]))
        return JsonResponse({'data': items})

    if 'category' in request.GET:
        order_option = request.GET.get("order-by", "name")
        context = {'items': Item.objects.filter(catid=request.GET['category']).order_by(order_by_values[order_option])}
        return render(request, 'catalog/index.html', context)

    items = Item.objects.all().order_by(order_by_values[order_option])
    context = {'items': items}
    return render(request, 'catalog/index.html', context)


def get_item_by_id(request, id):
    offers = Offer.objects.filter(itemid=id)
    highest_offer_dict = offers.aggregate(Max('amount'))
    highest_offer_amount = highest_offer_dict['amount__max']
    highest_offer = Offer.objects.filter(itemid=id, amount=highest_offer_amount).first()
    authuser = request.user
    buyer = User.objects.get(auth=authuser.id)
    return render(request, 'catalog/item_details.html', {
        'item': get_object_or_404(Item, pk=id),
        'offers': offers,
        'buyer': buyer,
        'highest_offer': highest_offer
    })


@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(request.POST, request.FILES)
        print(request.user)
        authuser = request.user
        user = User.objects.get(auth=authuser.id)
        if form.is_valid():
            item = Item()
            item.name = form.cleaned_data.get('name')
            item.condition = request.POST.get('condition')
            item.description = request.POST.get('description')
            item.buyout = request.POST.get('buyout')
            item.catid = form.cleaned_data.get('catid')
            item.image = request.FILES.get('image')
            item.sellerid = user
            item.save()
            messages.success(request, f'Item created!')
            return redirect('catalog-index')
        error_string = '\n'.join([' '.join(x for x in l) for l in list(form.errors.values())])
        messages.error(request, error_string)

    return render(request, 'catalog/create_item.html', {
        'form': ItemCreateForm()
    })


def delete_item(request, itemid):
    Item.objects.get(id=itemid).delete()
    return redirect('my_items')
