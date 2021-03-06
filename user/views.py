import json
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as AuthUser
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AccountCreationForm
from .models import User
from .models import Review
from catalog.models import Item
from offer.models import Offer
from django.contrib import messages


def get_user(auth_id):
    """Use the id of django's default user class to find the user in our database."""
    return User.objects.get(id=auth_id)


def register(request):
    """Create a new user in the django authenticated user database"""
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
    """Create a new user in our database"""
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User()
            user.name = request.POST.get('name')
            user.email = request.POST.get('email')
            user.bio = request.POST.get('bio')
            user.image = request.FILES.get('image')
            user.rating = 0
            user.id = AuthUser.objects.get(id=id)
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
    """View the account of the user who is currently logged in"""
    auth_id = request.user.id
    user = User.objects.get(id=auth_id)
    user_reviews = Review.objects.filter(user=user)
    try:
        accepted_offers = Offer.objects.filter(buyerid=user, accepted=True)
    except ObjectDoesNotExist:
        accepted_offers = None
    user_context = {
        'other_user': False,
        'user': user,
        'accepted_offers': accepted_offers,
        'reviews': user_reviews
    }
    return render(request, 'user/account.html', context=user_context)


def view_other_account(request, userid):
    """View the account of another user"""
    user_id = AuthUser.objects.get(username=userid).id
    user = User.objects.get(id=user_id)
    user_reviews = Review.objects.filter(user=user)
    user_context = {
        'other_user': True,
        'user': user,
        'accepted_offers': None,
        'reviews': user_reviews
    }
    return render(request, 'user/account.html', context=user_context)


def view_user_catalog(request, userid):
    """View all the items sold by a specific user"""
    user_id = AuthUser.objects.get(username=userid).id
    user = User.objects.get(id=user_id)
    items = Item.objects.filter(sellerid=userid)
    context = {"user": user, "items": items, "userid": userid}
    return render(request, 'user/user_catalog.html', context=context)


def view_my_items(request):
    """View the items sold by the user who is currently logged in"""
    user = get_user(request.user.id)
    try:
        user_items = Item.objects.filter(sellerid=user)
        context = {'user_items': user_items}
        return render(request, 'user/my_items.html', context)
    except ObjectDoesNotExist:
        return render(request, 'user/my_items.html')


def view_my_offers(request):
    """View the offers made by the user who is currently logged in"""
    user = get_user(request.user.id)
    try:
        user_offers = Offer.objects.filter(buyerid=user)
        item_list = []
        for offer in user_offers:
            item_list.append(Item.objects.get(id=offer.itemid.id))
        return render(request, 'user/my_offers.html', {'user_offers': user_offers, 'item_list': item_list})
    except ObjectDoesNotExist:
        return render(request, 'user/my_offers.html')


def view_account_settings(request):
    """Edit the account settings of the user who is currently logged in"""
    user = get_user(request.user.id)
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user.name = request.POST.get('name')
            user.email = request.POST.get('email')
            user.bio = request.POST.get('bio')
            form_image = request.FILES.get('image')
            if form_image:
                user.image = form_image
            user.save()
            messages.success(request, 'Account successfully changed.')
            return redirect('account')
        error_string = '\n'.join([' '.join(x for x in l) for l in list(form.errors.values())])
        messages.error(request, error_string)
    return render(request, 'user/account_settings.html', {
        'form': AccountCreationForm(initial={'name': user.name, 'email': user.email, 'bio': user.bio, 'image': user.image})
    })


def get_average_rating(userid):
    """Use the id of a user(our database, not django default) to look up their average rating"""
    user_id = AuthUser.objects.get(username=userid).id
    user = User.objects.get(id=user_id)
    reviews = Review.objects.filter(user=user)
    review_avg = reviews.aggregate(Avg('rating'))
    avg_rating = review_avg['rating__avg']
    return avg_rating


def rate_user(request, userid):
    """Create a new review for a user and post it, updating their average rating in the process"""
    if request.method == 'POST':
        user_id = AuthUser.objects.get(username=userid).id
        user = User.objects.get(id=user_id)
        new_review = Review()
        new_review.reviewer = get_user(request.user.id)
        new_review.user = user
        request_data = json.loads(request.body)
        new_review.rating = request_data['rating']
        new_review.review = request_data['review']
        new_review.save()
        new_rating = get_average_rating(userid)
        user.rating = new_rating
        user.save()
        return redirect(f'../{userid}')
