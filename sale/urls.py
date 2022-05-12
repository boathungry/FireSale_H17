from django.urls import path
from . import views
urlpatterns = [
    # http/localhost:8000/candies
    path('buyout_item', views.view_buyout_item, name='buyout_item'),
    path('buyout_item/<id>', views.create_checkout, name='create_checkout'),
    path('billing_checkout/<id>', views.create_billing, name='billing_checkout'),
    path('billing_checkout', views.view_billing, name='billing_checkout'),
    path('checkout_overview/<id>', views.view_checkout_overview, name='checkout_overview')

]