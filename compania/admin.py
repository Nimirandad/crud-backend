from django.contrib import admin
from .models import *

# Register your models here.


class CiudadAdmin(admin.ModelAdmin):
    fields = ['nombre_ciudad']


class TituloAdmin(admin.ModelAdmin):
    fields = ['nombre_titulo']

class EmpleadoAdmin(admin.ModelAdmin):
    fields = ['nombre_empleado', 'ciudad_empleado', 'titulo_empleado']

admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Titulo, TituloAdmin)
admin.site.register(Empleado, EmpleadoAdmin)