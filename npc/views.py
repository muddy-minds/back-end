from django.shortcuts import render

from rest_framework import viewsets, mixins

from adv.models import Npc
from .serializers import NpcSerializer


class NpcViewSet(viewsets.ModelViewSet):
    queryset = Npc.objects.all()
    serializer_class = NpcSerializer
