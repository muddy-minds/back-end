from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Q

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    items = ArrayField(
        models.IntegerField(default=0),
        size=100,
    )
    north = models.IntegerField(default=0)
    south = models.IntegerField(default=0)
    east = models.IntegerField(default=0)
    west = models.IntegerField(default=0)

    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()

    def __str__(self):
        return self.name

# https://django-postgres-extensions.readthedocs.io/en/latest/arrays.html
# array field methods 
class Player(models.Model):
    name = models.CharField(max_length=50)
    items = ArrayField(
        models.IntegerField(default=0),
        size=100,
    )
    description = models.CharField(max_length=500)
    health_points = models.FloatField()
    lives = models.IntegerField(default=3)
    room_id = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True)

    def getItem(self, item):
        if isInstance(RoomItems) & item.room_id == room_id:
            item.player_id = id 
            Player.objects.update(items = ArrayAppend('items', item.id))


    def dropItem(self, item):
        if item.player_id == id:
            item.player_id = None
            Player.objects.update(items = ArrayRemove('items', item.id))

    def readItem(self, item):
        return item.description 

    def eatItem(self, foodItem):
        if isInstance(foodItem, FoodItem):
            health_points += foodItem.health_points
    
    def enterNewRoom(self, command):
        if type(command) == str:
            if command == "n":
                if Room.objects.get(id=room_id).north != 0:
                    room_id = Room.objects.get(id=room_id).north
                else:
                    print("We cannot go north")
            elif command == "s":
                if Room.objects.get(id=room_id).south !=0 :
                    room_id = Room.objects.get(id=room_id).south
                else:
                    print("We cannot go south")
            elif command == "w":
                if Room.objects.get(id=room_id).west !=0:
                    room_id = Room.objects.get(id=room_id).west
                else:
                    print("We cannot go west")
            elif command == "e":
                if Room.objects.get(id=room_id).east !=0:
                    room_id = Room.objects.get(id=room_id).east 
                else:
                    print("We cannot go east")



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
