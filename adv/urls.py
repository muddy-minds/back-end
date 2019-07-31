from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import RoomViewSet, PlayerViewSet


router = DefaultRouter()
# router.register('rooms', RoomViewSet)
# router.register('players', PlayerViewSet)

app_name = 'adv'

urlpatterns = [
    path('', include(router.urls))
]