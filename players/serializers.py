from rest_framework import serializers

from adv.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""
    class Meta:
        model = Player
        fields = ('id', 'name', 'items', 'health_points', 'lives', 'room_id')
        read_only_fields = ('id',)