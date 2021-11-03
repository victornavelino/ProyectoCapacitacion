from django.contrib import admin

# Register your models here.
from .models import Capacitacion
from .models import area.Area


class AreaInline(admin.TabularInline):
    model = Area


class CapacitacionAdmin(admin.ModelAdmin):
    inlines = [AreaInline]


#admin.site.register(Capacitacion)
admin.site.register(Area)
admin.site.register(Capacitacion, CapacitacionAdmin)

