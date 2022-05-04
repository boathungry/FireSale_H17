from django.urls import path
from . import views
urlpatterns = [
    # http/localhost:8000/candies
    path('', views.index, name="catalog-index"),
    path('<int:id>', views.get_category_by_id, name='category-details'),
    path('create_item', views.create_item, name='create_item'),

]