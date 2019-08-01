from rest_framework import serializers

from adv.models import Toys

class ToysSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""
    class Meta:
        model = Toys
        fields = ('id', 'name', 'description', 'room_id', 'some_points', 'player_id')
        read_only_fields = ('id',)
