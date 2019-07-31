from rest_framework import viewsets, mixins

from adv.models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.GenericViewSet, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
