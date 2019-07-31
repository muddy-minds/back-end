from rest_framework import serializers

from adv.models import Room, Player

class RoomSerializer(serializers.ModelSerializer):
    """Serializer for room objects"""
    class Meta:
        model = Room
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)

class PlayerSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""
    class Meta:
        model = Player
        fields = ('id', 'name', 'items', 'health_points', 'lives', 'room_id')
        read_only_fields = ('id',)