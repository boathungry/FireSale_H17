from django.shortcuts import render, get_object_or_404
from catalog.models import Category


# Create your views here.

def index(request):
    context = {'category': Category.objects.all().order_by('name')}
    return render(request, 'electronics/index.html', context)

def get_category_by_id(request, id):
    return render(request, 'catalog/catalog_category_details.html', {
        'category': get_object_or_404(Category, pk=id)
    })