from django.contrib import admin

# Register your models here.
from .models import Capacitacion
from .models import Area

admin.site.register(Capacitacion)
admin.site.register(Area)