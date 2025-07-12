from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('template.html')  # ✅ Fixed here
    context = {
        'members': mydata,
    }
    return HttpResponse(template.render(context, request))
