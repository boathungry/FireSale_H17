from django.shortcuts import render, get_object_or_404
from catalog.models import Category


# Create your views here.

def index(request):
    context = {'categories': Category.objects.all().order_by('name')}
    return render(request, 'catalog/index.html', context)



def get_category(request,pk):
    return render(request, 'catalog/catalog_category_details.html', {
        'category': get_object_or_404(Category, pk)
    })



