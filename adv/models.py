from django.contrib.postgres.fields import ArrayField
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    north = models.IntegerField(default=0)
    south = models.IntegerField(default=0)
    east = models.IntegerField(default=0)
    west = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=50)
    items = ArrayField(
        models.CharField(max_length=50, blank=True),
        size=100,
    )
    description = models.CharField(max_length=500)
    health_points = models.FloatField()
    lives = models.IntegerField(default=3)
    room_id = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True)


class Npc(models.Model):
    name = models.CharField(max_length=50)
    friend_id = models.ForeignKey(
        Player, models.SET_NULL, blank=True, null=True)
    health_points = models.FloatField()
    lives = models.IntegerField(default=3)
    room_id = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=500)


class RoomItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    room_id = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True)
    player_id = models.ForeignKey(
        Player, models.SET_NULL, blank=True, null=True)

    class Meta:
        abstract = True


class FoodItem(RoomItems):
    health_points = models.FloatField()


class Toys(RoomItems):
    some_points = models.FloatField()


class Weapons(RoomItems):
    damage_points = models.FloatField()
