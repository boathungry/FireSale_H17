from django.urls import path
from . import views
urlpatterns = [
    # http/localhost:8000/candies
    path('buyout_item/<int:id>', views.create_checkout, name='buyout_item'),
    path('billing_checkout/<id>', views.create_billing, name='billing_checkout'),
    path('checkout_overview/<id>', views.view_checkout_overview, name='checkout_overview')

]