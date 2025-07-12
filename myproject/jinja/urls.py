from django.urls import path
from . import views

urlpatterns = [
    path('', views.displaygreen, name='displaygreen'),
    ]