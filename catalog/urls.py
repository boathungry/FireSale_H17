from django.template.defaulttags import url
from django.urls import path
from . import views

urlpatterns = [
    # http/localhost:8000/catalog
    path('', views.index, name="catalog-index"),
    path('<int:id>', views.get_item_by_id, name='item_details'),
    path('create_item', views.create_item, name='create_item'),
    path('delete_item/<int:itemid>', views.delete_item, name='delete_item')
]

