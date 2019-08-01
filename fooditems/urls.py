from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FoodItemViewSet


router = DefaultRouter()
router.register('', FoodItemViewSet)
# router.register('/api/fooditems', FoodItemViewSet)



app_name = 'fooditems'

urlpatterns = [
    path('', include(router.urls)),
]
