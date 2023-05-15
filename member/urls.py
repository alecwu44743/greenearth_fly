from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # login/logout/register
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
    
    path('staff_login', views.staff_login, name='staff_login'),
    path('staff_register', views.staff_register, name='staff_register'),
]