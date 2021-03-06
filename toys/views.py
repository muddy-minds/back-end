from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets, mixins

from adv.models import Toys
from .serializers import ToysSerializer


class ToysViewSet(viewsets.ModelViewSet):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer
