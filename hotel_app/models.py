from django.db import models

# Create your models here.

class Room(models.Model):
    numero = models.PositiveIntegerField(blank=False, unique=True)
    ocupado = models.BooleanField(blank=False, default=False)
    detalle = models.CharField(max_length=400, blank=False)
    precio = models.FloatField(blank=False)
    dormitorios = models.IntegerField(blank=False)
    capacidad = models.IntegerField(blank=False)


class User(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    direccion = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    telefono = models.IntegerField(max_length=12, blank=False)
    cp = models.CharField(max_length=6, blank=False)