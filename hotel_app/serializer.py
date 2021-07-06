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
    class Meta: 
        model = Booking
        fields = '__all__'