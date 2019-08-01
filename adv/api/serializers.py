from rest_framework import serializers

from adv.models import Room, Player, Npc, FoodItem, Toys, Weapons

class RoomSerializer(serializers.ModelSerializer):
    """Serializer for room objects"""
    class Meta:
        model = Room
        fields = ('id', 'name', 'description', 'north', 'south', 'east', 'west')
        read_only_fields = ('id',)

class PlayerSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""
    class Meta:
        model = Player
        fields = ('id', 'name', 'items', 'description', 'health_points', 'lives', 'room_id')
        read_only_fields = ('id',)

class NpcSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""
    class Meta:
        model = Npc
        fields = ('id', 'name', 'friend_id', 'description', 'health_points', 'lives', 'room_id')
        read_only_fields = ('id',)
