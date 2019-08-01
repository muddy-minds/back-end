from django.shortcuts import render
from rest_framework import viewsets, mixins

from adv.models import FoodItem
from .serializers import FoodItemSerializer


class FoodItemViewSet(viewsets.GenericViewSet, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
