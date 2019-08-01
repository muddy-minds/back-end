from rest_framework import serializers

from adv.models import Npc

class NpcSerializer(serializers.ModelSerializer):
    """Serializer for Npc objects"""
    class Meta:
        model = Npc
        fields = ('id', 'name', 'description', 'friend_id', 'health_points', 'lives', 'room_id')
        read_only_fields = ('id',)

