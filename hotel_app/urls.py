from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()

router.register('rooms', RoomViewset)
router.register('users', UserViewset)
router.register('bookings', BookingViewset)

urlpatterns = router.urls