from django.urls import path
from . import views
urlpatterns = [
    # http/localhost:8000/candies
    path('buyout_item', views.view_buyout_item, name='buyout_item'),
    path('buyout_item/<id>', views.create_checkout, name='create_checkout'),
]