from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as AuthUser
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AccountCreationForm
from .models import User
from catalog.models import Item
from offer.models import Offer
from django.contrib import messages


def get_user(auth_id):
    return User.objects.get(auth=auth_id)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect(f'create_account/{user.id}')
        error_string = '\n'.join([' '.join(x for x in l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def create_account(request, id):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User()
            user.name = request.POST.get('name')
            user.email = request.POST.get('email')
            user.bio = request.POST.get('bio')
            user.image = request.FILES.get('image')
            user.rating = 0
            user.auth = AuthUser.objects.get(id=id)
            user.save()
            messages.success(request, f'Account created for {user.name}!')
            return redirect('login')
        error_string = '\n'.join([' '.join(x for x in l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    else:
        form = AccountCreationForm()
    return render(request, 'user/create_account.html', {
        'form': form
    })


def view_account(request):
    auth_id = request.user.id
    user = User.objects.get(auth=auth_id)
    user_context = {'user_name': user.name, 'user_bio': user.bio, 'user_image': user.image, 'user_rating': user.rating}
    return render(request, 'user/account.html', context=user_context)


def view_my_items(request):
    user = get_user(request.user.id)
    try:
        user_items = Item.objects.filter(sellerid=user.id)
        context = {'user_items': user_items}
        return render(request, 'user/my_items.html', context)
    except ObjectDoesNotExist:
        return render(request, 'user/my_items.html')


def view_my_offers(request):
    user = get_user(request.user.id)
    try:
        user_offers = Offer.objects.filter(buyerid=user.id)
        item_list = []
        for offer in user_offers:
            item_list.append(Item.objects.get(id=offer.itemid.id))
        return render(request, 'user/my_offers.html', {'user_offers': user_offers, 'item_list': item_list})
    except ObjectDoesNotExist:
        return render(request, 'user/my_offers.html')


def view_account_settings(request):
    user = get_user(request.user.id)
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user.name = request.POST.get('name')
            user.email = request.POST.get('email')
            user.bio = request.POST.get('bio')
            user.image = request.FILES.get('image')
            user.save()
            messages.success(request, 'Account successfully changed.')
            return redirect('account')
        error_string = '\n'.join([' '.join(x for x in l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    return render(request, 'user/account_settings.html', {
        'form': AccountCreationForm(initial={'name': user.name, 'email': user.email, 'bio': user.bio, 'image': user.image})
    })


