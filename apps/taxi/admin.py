from django.contrib import admin
from .models import Vehiculo,Rol,Viaje, Usuario

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Rol)
admin.site.register(Viaje)
admin.site.register(Usuario)
