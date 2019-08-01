from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ToysViewSet


router = DefaultRouter()
router.register('', ToysViewSet)



app_name = 'toys'

urlpatterns = [
    path('', include(router.urls)),
]