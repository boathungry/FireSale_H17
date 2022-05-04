from django.template.defaulttags import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^get_category/(?P<pk>\d+)$', views.get_category_by, name='get_category'),
    path('<int:id>', views.get_category_by_id, name='category-details'),

]

