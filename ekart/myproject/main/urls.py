from django.urls import path
from . import views

urlpatterns = [
    path('', views.canteen_list, name='canteen_list'),
    path('canteen/<int:pk>/', views.canteen_detail, name='canteen_detail'),
]