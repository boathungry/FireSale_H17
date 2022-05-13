from django.shortcuts import render, redirect
from user.models import User
from catalog.models import Item

# Create your views here.


def index(request):
    """View the home page"""
    authid = request.user.id
    user = User.objects.filter(id=authid)
    user_items = Item.objects.filter(sellerid=authid)
    items = Item.objects.filter(offer_accepted=False).order_by("-id")
    context = {"user": user, "items": items, "user_items": user_items}
    return render(request, 'layout/index.html', context=context)


def view_about(request):
    """View the about page"""
    authid = request.user.id
    user = User.objects.filter(id=authid)
    return render(request, 'layout/about.html', context={"user": user})
