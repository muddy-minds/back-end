from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WeaponsViewSet


router = DefaultRouter()
router.register('', WeaponsViewSet)


app_name = 'weapons'

urlpatterns = [
    path('', include(router.urls)),
]