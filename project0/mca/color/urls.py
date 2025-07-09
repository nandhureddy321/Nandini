from django.urls import path
from .import views

urlpatterns=[
    path('red/',views.red,name='red'),
    path('pink/',views.pink,name='pink'),
    path('blue/',views.blue,name='blue'),
    path('sushma/',views.sushma,name='sushma'),
    path('kiran/',views.kiran,name='kiran'),
    path('divya/',views.divya,name='divya'),
]