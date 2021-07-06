from django.db import models

# Create your models here.

class Room(models.Model):
    numero = models.PositiveIntegerField(blank=False, unique=True)
    ocupado = models.BooleanField(blank=False, default=False)
    detalle = models.CharField(max_length=400, blank=False)
    precio = models.FloatField(blank=False)
    dormitorios = models.IntegerField(blank=False)
    capacidad = models.IntegerField(blank=False)
    
    def __str__(self):
        return (str(self.numero))



class User(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    direccion = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=False)
    telefono = models.IntegerField(max_length=14, blank=False)
    cp = models.CharField(max_length=6, blank=True)
    
    
    def __str__(self):
        return (self.nombre)

lista_estados = [
    ('PENDIENTE', 'PENDIENTE'),
    ('PAGADO', 'PAGADO'),
    ('ELIMINADO', 'ELIMINADO'),
]

lista_metodos_pago = [
    ('EFECTIVO', 'EFECTIVO'),
    ('TRANSFERENCIA', 'TRANSFERENCIA'),
    ('CHEQUE', 'CHEQUE'),
    ('TARJETA', 'TARJETA'),
    ('CRIPTODIVISA', 'CRIPTODIVISA'),
]

class Booking(models.Model):
    fk_cliente = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, unique=False)
    fk_habitacion = models.ForeignKey(Room, blank=False, on_delete=models.DO_NOTHING)
    estado = models.CharField(max_length=45, choices=lista_estados, default=lista_estados[0], blank=False)
    metodo_pago = models.CharField(max_length=45, choices=lista_metodos_pago, blank=True)
    monto_pagado = models.FloatField(blank=False, default=0)
    dias_reserva = models.PositiveIntegerField(blank=False, default=1) 