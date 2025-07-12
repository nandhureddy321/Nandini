from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bakery_list, name='Bakery_list'),
    path('Bakery/<int:pk>/', views.Bakery_detail, name='Bakery_detail'),
]


urlpatterns = [
    path('', views. mess_list, name=' mess_list'),
    path(' mess/<int:pk>/', views. mess_detail, name=' mess_detail'),
]


urlpatterns = [
    path('', views.canteen_list, name='canteen_list'),
    path('canteen/<int:pk>/', views.canteen_detail, name='canteen_detail'),
]