from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import AccountCreationForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_account')
    return render(request, 'user/register.html', {
        'form':UserCreationForm()
    })


def create_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(data=request.POST)
        if form.is_valid():
            user = User()
            user.name = request.POST.get('name')
            user.bio = request.POST.get('bio')
            user.image = request.POST.get('image')
            user.rating = 0
            user.auth = request.user
            user.save()
            return redirect('login')
    else:
        form = AccountCreationForm()
    return render(request, 'user/create_account.html', {
        'form':AccountCreationForm()
    })