from django.urls import path
from . import views


urlpatterns = [
    path('make_offer/<int:id>', views.make_offer, name='make_offer'),
    path('cancel_offer/<int:id>', views.cancel_offer, name='cancel_offer')
]