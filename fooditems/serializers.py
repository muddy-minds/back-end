from rest_framework import serializers

from adv.models import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'description', 'room_id', 'health_points', 'player_id')
        read_only_fields = ('id',)

