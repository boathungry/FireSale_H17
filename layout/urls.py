from django.urls import path
from . import views
urlpatterns = [
    # http/localhost:8000/candies
    path('', views.index, name="LayOut-index"),
    path('about', views.view_about, name='about'),
]