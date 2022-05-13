from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from user.models import User
from catalog.models import Item

# Create your views here.


def index(request):
    """View the home page"""
    authid = request.user.id
    try:
        user = User.objects.get(id=authid)
    except ObjectDoesNotExist:
        user = None
    user_items = Item.objects.filter(sellerid=user)
    items = Item.objects.filter(offer_accepted=False).order_by("-id")
    context = {"user": user, "items": items, "user_items": user_items}
    return render(request, 'layout/index.html', context=context)


def view_about(request):
    """View the about page"""
    return render(request, 'layout/about.html')
