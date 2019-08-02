from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# class RoomItemField(models.Field):
#     description = models.CharField(max_length=500)

#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = 104
#         super().__init__(*args, **kwargs)

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    items = JSONField(default={})
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
                self.north = destinationRoomID
            elif direction == "s":
                self.south = destinationRoomID
            elif direction == "e":
                self.east = destinationRoomID
            elif direction == "w":
                self.west = destinationRoomID
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
    items = JSONField(default={})
    description = models.CharField(max_length=500)
    health_points = models.FloatField()
    lives = models.IntegerField(default=3)
    currentRoom = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True)
 
    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()

    # def enterNewRoom(self, command):
    #     if type(command) == str:
    #         if command == "n":
    #             if Room.objects.get(id=room_id).north != 0:
    #                 room_id = Room.objects.get(id=room_id).north
    #             else:
    #                 print("We cannot go north")
    #         elif command == "s":
    #             if Room.objects.get(id=room_id).south !=0 :
    #                 room_id = Room.objects.get(id=room_id).south
    #             else:
    #                 print("We cannot go south")
    #         elif command == "w":
    #             if Room.objects.get(id=room_id).west !=0:
    #                 room_id = Room.objects.get(id=room_id).west
    #             else:
    #                 print("We cannot go west")
    #         elif command == "e":
    #             if Room.objects.get(id=room_id).east !=0:
    #                 room_id = Room.objects.get(id=room_id).east 
    #             else:
    #                 print("We cannot go east")

    # def befriendNPC(self, NPC):
    #     if isinstance(NPC, Npc) & NPC.friend_id != None:
    #         NPC.friend_id = id
    #         print("You are now friends with", NPC.name)

    # def defriendNPC(self, NPC):
    #     if isinstance(NPC, Npc) & NPC.friend_id == id:
    #         NPC.friend_id = None
    #         print("You are not friends with", NPC.name)



class Npc(models.Model):
    name = models.CharField(max_length=50)
    friend_id = models.ForeignKey(
        Player, models.SET_NULL, blank=True, null=True)
    health_points = models.FloatField()
    lives = models.IntegerField(default=3)
    room_id = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=500)


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()