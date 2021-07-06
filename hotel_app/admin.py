from django.contrib import admin
from .models import *
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    model = Room 
    list_display = ('numero', 'ocupado', 'detalle', 'precio', 'dormitorios', 'capacidad')

class UserAdmin(admin.ModelAdmin):
    model = User 
    list_display = ('nombre', 'direccion', 'email', 'telefono', 'cp')

class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('get_nombre', 'estado', 'metodo_pago', 'monto_pagado', 'dias_reserva', 'get_email', 'get_telefono', 'get_direccion', 'get_cp', 'get_numero', 'get_detalle', 'get_precio', 'get_dormitorios', 'get_capacidad')

    def get_numero(self, obj):
        return obj.fk_habitacion.numero
    get_numero.admin_order_field = 'fk_habitacion'
    get_numero.short_description = 'Numero'
    
    def get_detalle(self, obj):
        return obj.fk_habitacion.detalle
    get_detalle.admin_order_field = 'fk_habitacion'
    get_detalle.short_description = 'detalle'

    def get_precio(self, obj):
        return obj.fk_habitacion.precio
    get_precio.admin_order_field = 'fk_habitacion'
    get_precio.short_description = 'Precio'

    def get_dormitorios(self, obj):
        return obj.fk_habitacion.dormitorios
    get_dormitorios.admin_order_field = 'fk_habitacion'
    get_dormitorios.short_description = 'Dormitorios'

    def get_capacidad(self, obj):
        return obj.fk_habitacion.capacidad
    get_capacidad.admin_order_field = 'fk_habitacion'
    get_capacidad.short_description = 'Capacidad'


    def get_nombre(self, obj):
        return obj.fk_cliente.nombre
    get_nombre.admin_order_field = 'fk_cliente'
    get_nombre.short_description = 'Cliente'

    def get_direccion(self, obj):
        return obj.fk_cliente.direccion
    get_direccion.admin_order_field = 'fk_cliente'
    get_direccion.short_description = 'Direccion'

    def get_email(self, obj):
        return obj.fk_cliente.email
    get_email.admin_order_field = 'fk_cliente'
    get_email.short_description = 'Email'

    def get_telefono(self, obj):
        return obj.fk_cliente.telefono
    get_telefono.admin_order_field = 'fk_cliente'
    get_telefono.short_description = 'Telefono'

    def get_cp(self, obj):
        return obj.fk_cliente.cp
    get_cp.admin_order_field = 'fk_cliente'
    get_cp.short_description = 'Cp'

admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Booking, BookingAdmin)