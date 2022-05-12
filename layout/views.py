from django.shortcuts import render, redirect
from user.models import User

# Create your views here.
def index(request):
    auth_id = request.user.id
    user = User.objects.get(auth=auth_id)
    context = {'user_image': user.image}
    return render(request, 'layout/index.html', context)

def view_about(request):
    return render(request, 'layout/about.html')
