# Desarrollá los endpoints para el sistema de reservas de habitación de un hotel.

#### CONDICIONES:
- Las reservas pueden tener 3 estados: Pendiente, Pagado y Eliminado.
- Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.
- Proponé los endpoints a crearse para tratar de cubrir el flujo normal de operación de reserva y explicar por qué, además de desarrollarlos.
  Luego que tengas ya todo el código
  -Crear un repositorio para la entrega del código y en un readme del repositorio la justificación de los endpoints creados

#### Tecnologías utilizadas
- Python
- Django
- Rest Framework


#### ENDPOINTS

* ##### Users
    *   /users        [GET, POST] -> Obtener una lista de usuarios / registrar nuevos usuarios
    *   /users/:id    [GET, PUT, PATCH, DELETE] -> (Obtener los datos / modificiar los datos / modificar un dato / eliminar el registro) de un usuario en particular
* ##### Rooms
    *   /rooms        [GET, POST] -> Obtener una lista de todos las habitaciones pertenecientes al hotel / registrar nuevas habitaciones
    *   /rooms/:id    [GET, PUT, PATCH] -> (Obtener los datos / modificiar los datos / modificar un dato ) de una habitacion en particular
* ##### Bookings
    *   /bookings     [GET, POST] -> Obtener una lista de todos las reservas pertenecientes al hotel / registrar nuevas reservas
    *   /bookings/:id [GET, PUT, PATCH, DELETE] -> (Obtener los datos / modificiar los datos / modificar un dato / eliminar el registro) de una reserva en particular



#### Ejemplos:

##### /users [GET]
```
[
  {
    "id": 1,
    "nombre": "Pedro Aznar",
    "direccion": "Gorostiaga",
    "email": "pedro@mailinator.com",
    "telefono": 5555555555,
    "cp": "W6500"
  },
  {
    "id": 2,
    "nombre": "Manuel Madariaga",
    "direccion": "Loreto",
    "email": "manuel@mailinator.com",
    "telefono": 5555555556,
    "cp": "E2000"
  },
]
```

##### /users [POST]
``` body
{
  'nombre': 'Leonardo Starosta',
  'email': 'leonardo@mailinator.com',
  'telefono': 5551234555,
  'cp' : 'O1220',
  'direccion': 'Altamira'
}
```

##### /rooms/1 [GET]
```
{
  "id": 1,
  "numero": 1,
  "ocupado": true,
  "detalle": "Amplio y comodo",
  "precio": 15000.0,
  "dormitorios": 3,
  "capacidad": 7
}
```

##### /rooms [POST]
```
{
  "numero": '16',
  "ocupado": False,
  "detalle": 'Amplio, baños en suite',
  "precio": 21000.0,
  "dormitorios": 5,
  "capacidad": 9
  
}
```

##### /bookings [POST]
```
{
  'fk_cliente': 1,
  'fk_habitacion': 3,
  'estado': 'PAGADO',
  'metodo_pago': 'TRANSFERENCIA',
  'monto_pagado': 21000.0,
  'dias_reserva': 4,
}
```

##### Hecho con :heart:
