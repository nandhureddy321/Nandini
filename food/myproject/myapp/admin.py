from django.contrib import admin
from .models import Bakery
from .models import mess
from .models import canteen
# Register your models here.

admin.site.register(Bakery)
admin.site.register(mess)
admin.site.register(canteen)

