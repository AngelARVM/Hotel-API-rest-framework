from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
from .serializer import *
from .models import *

class RoomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'nombre': request.data.get('nombre'), 
    #         'direccion': request.data.get('direccion'), 
    #         'email': request.data.get('email'), 
    #         'telefono': request.data.get('telefono'), 
    #         'cp': request.data.get('cp'), 
    #     }
    #     serializer = RoomSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    

