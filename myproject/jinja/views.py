from django.shortcuts import render

# Create your views here.
def displaygreen(request):
    stu=[{'name':'shiva','marks':90},{'name':'navmohan','marks':85},
         {'name':'shravani','marks':88},{'name':'salma','marks':91}]

    return render(request,'green.html',{'data': stu})

##def displaygreen(request):
##    stu=['shiva','navmohan','shravani','salma']
##    return render(request,'green.html',{'data': stu})