from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets, mixins

from adv.models import Weapons
from .serializers import WeaponsSerializer


class WeaponsViewSet(viewsets.ModelViewSet):
    queryset = Weapons.objects.all()
    serializer_class = WeaponsSerializer
