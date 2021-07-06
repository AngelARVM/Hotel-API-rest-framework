from django.contrib import admin
from .models import *
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ocupado', 'detalle', 'precio', 'dormitorios', 'capacidad')

class UserAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'email', 'telefono', 'cp')

admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)