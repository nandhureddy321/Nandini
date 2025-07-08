from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
##create your veiws here.
def home(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())