from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NpcViewSet


router = DefaultRouter()
router.register('', NpcViewSet)



app_name = 'npc'

urlpatterns = [
    path('', include(router.urls)),
]