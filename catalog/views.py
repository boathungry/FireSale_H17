from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Category, Item
from django.contrib.auth.decorators import login_required
from user.models import User



# Create your views here.
from forms.item_form import ItemCreateForm


def index(request):
    if 'category' in request.GET:
        context = {'items': Item.objects.filter(catid__item=request.GET['category'])}
        return render(request, 'catalog/index.html', context)
    Items = Item.objects.all().order_by('name')
    context = {'items': Items}
    return render(request, 'catalog/index.html', context)



def get_item_by_id(request, id):
    return render(request, 'catalog/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
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
            item.image = form.cleaned_data.get('image')
            item.sellerid = user
            item.save()
            return redirect('catalog-index')
    else:
        form = ItemCreateForm()
    return render(request, 'catalog/create_item.html', {
        'form': form
    })

