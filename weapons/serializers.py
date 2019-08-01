from rest_framework import serializers

from adv.models import Weapons

class WeaponsSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""
    class Meta:
        model = Weapons
        fields = ('id', 'name', 'description', 'room_id', 'damage_points', 'player_id')
        read_only_fields = ('id',)