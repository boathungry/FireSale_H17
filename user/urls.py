from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name='register'),
    path('create_account/<id>', views.create_account, name='create_account'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('account', views.view_account, name='account'),
    path('my_items', views.view_my_items, name='my_items'),
    path('my_offers', views.view_my_offers, name='my_offers'),
    path('account_settings', views.view_account_settings, name='account_settings'),
    path('<userid>', views.view_other_account, name='other_account'),
    path('<userid>/catalog', views.view_user_catalog, name='user_catalog'),
    path('<userid>/rate', views.rate_user, name='rate_user')
]