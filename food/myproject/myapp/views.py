from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Bakery


def Bakery_list(request):
    ob_Bakerys = Bakery.objects.all()
    return render(request, 'bakery_list.html', {'bakerys': ob_Bakeerys})

def Bakery_detail(request, pk):
    ob_Bakeery = get_object_or_404(bakery, pk=pk)
    return render(request, 'Bakery_detail.html', {'Bakery': ob_Bakery})


from django.shortcuts import render, get_object_or_404
from .models import mess


def mess_list(request):
    ob_mess= mess.objects.all()
    return render(request, 'mess_list.html', {'mess': ob_mess})

def mess_detail(request, pk):
    ob_mess = get_object_or_404(bakery, pk=pk)
    return render(request, 'mess_detail.html', {'mess': ob_mess})

from django.shortcuts import render, get_object_or_404
from .models import canteen


def canteen_list(request):
    ob_canteens = canteen.objects.all()
    return render(request, 'canteen_list.html', {'canteens': ob_canteens})

def canteen_detail(request, pk):
    ob_canteen = get_object_or_404(canteen, pk=pk)
    return render(request, 'canteen_detail.html', {'canteen': ob_canteen})

