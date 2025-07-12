# members/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.testing, name='Member'),
   
]
