from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # newFlight
    path('newFlight', views.newFlight, name='newFlight'),
]