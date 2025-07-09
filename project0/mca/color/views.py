from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def red(request):
      return render(request,'red.html')

def pink(request):
      return render(request,'pink.html')

def blue(request):
      return render(request,'blue.html')

def sushma(request):
      return render(request,'sushma.html')

def kiran(request):
      return render(request,'kiran.html')

def divya(request):
      return render(request,'divya.html')