from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Room
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = serializers.ReadOnlyField(source='fk_habitacion.numero')
    ocupado = serializers.ReadOnlyField(source='fk_habitacion.ocupado')
    detalle = serializers.ReadOnlyField(source='fk_habitacion.detalle')
    precio = serializers.ReadOnlyField(source='fk_habitacion.precio')
    dormitorios = serializers.ReadOnlyField(source='fk_habitacion.dormitorios')
    capacidad = serializers.ReadOnlyField(source='fk_habitacion.capacidad')

    nombre = serializers.ReadOnlyField(source='fk_cliente.nombre')
    direccion = serializers.ReadOnlyField(source='fk_cliente.direccion')
    email = serializers.ReadOnlyField(source='fk_cliente.email')
    telefono = serializers.ReadOnlyField(source='fk_cliente.telefono')
    cp = serializers.ReadOnlyField(source='fk_cliente.cp')
    
    class Meta: 
        model = Booking
        fields =  ('id', 'estado', 'metodo_pago', 'room', 'ocupado', 'detalle', 'precio', 'dormitorios', 'capacidad', 'nombre', 'direccion', 'email', 'telefono', 'cp')

