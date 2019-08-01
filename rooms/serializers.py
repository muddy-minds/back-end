from rest_framework import serializers

from adv.models import Room

class RoomSerializer(serializers.ModelSerializer):
    """Serializer for room objects"""
    class Meta:
        model = Room
        fields = ('id', 'name', 'description', 'north', 'south', 'east', 'west', 'items')
        read_only_fields = ('id',)

