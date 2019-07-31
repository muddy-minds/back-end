from rest_framework import viewsets, mixins

from adv.models import Room
from .serializers import RoomSerializer

class RoomViewSet(viewsets.GenericViewSet, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

