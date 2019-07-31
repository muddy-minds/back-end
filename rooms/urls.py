from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet


router = DefaultRouter()
router.register('', RoomViewSet)



app_name = 'rooms'

urlpatterns = [
    path('', include(router.urls)),
]