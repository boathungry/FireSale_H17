from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Item


# Create your views here.

def index(request):
    if 'category' in request.GET:
        context = {'items': Item.objects.filter(catid__item=request.GET['category'])}
        return render(request, 'catalog/index.html', context)
    Items = Item.objects.all().order_by('name')
    context = {'items': Items}
    return render(request, 'catalog/index.html', context)



def get_category_by_id(request, id):
    return render(request, 'catalog/catalog_category_details.html', {
        'category': get_object_or_404(Category, pk=id)
    })

