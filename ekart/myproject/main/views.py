from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Canteen

def canteen_list(request):
    canteens = Canteen.objects.all()
    return render(request, 'canteen_list.html', {'canteens': canteens})

def canteen_detail(request, pk):
    canteen = get_object_or_404(Canteen, pk=pk)
    return render(request, 'canteen_detail.html', {'canteen': canteen})
