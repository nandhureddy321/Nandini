from django.urls import path
from .views import (
    EmployeeCreateView, EmployeeListView,
    EmployeeUpdateView, EmployeeDeleteView
)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]