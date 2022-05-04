from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Category, Item


# Create your views here.
from forms.item_form import ItemCreateForm


def index(request):
    if 'category' in request.GET:
        context = {'items': Item.objects.filter(catid__item=request.GET['category'])}
        return render(request, 'catalog/index.html', context)
    Items = Item.objects.all().order_by('name')
    context = {'items': Items}
    return render(request, 'catalog/index.html', context)



def get_category(request,pk):
    return render(request, 'catalog/catalog_category_details.html', {
        'category': get_object_or_404(Category, pk)
    })


def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('candy-index')
    else:
        form = ItemCreateForm()
    return render(request, 'catalog/create_item.html', {
        'form': form
    })

