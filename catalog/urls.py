from django.urls import path
from . import views
urlpatterns = [
    # http/localhost:8000/candies
    path('', views.index, name="electronics-index"),
    path('<int:id>', views.get_category_by_id, name='category-details'),

]