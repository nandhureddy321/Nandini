from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Employee

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'department', 'join_date']
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee_list.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'department', 'join_date']
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

# Create your views here.
