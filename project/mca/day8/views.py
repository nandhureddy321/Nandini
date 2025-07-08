from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import studentModel  
from .forms import studentForm
#display & save form data   
def insert_student(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = studentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_student.html", context)  
