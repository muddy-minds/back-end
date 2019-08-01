from rest_framework import viewsets, mixins

from adv.models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        """Retrive the player for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

    
    def get_serializer_class(self):
        """Return the serializer class"""
        if self.action == 'retrieve':
            return serializers.PlayerSerializer
        
        return self.serializer_class

    def create_player(sef, serializer):
        """Create a new player"""
        serializer.save(user=self.request.user)
