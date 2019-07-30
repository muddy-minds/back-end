from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
# class Room(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=500)
#     north = models.IntegerField(default=0)
#     south = models.IntegerField(default=0)
#     east = models.IntegerField(default=0)
#     west = models.IntegerField(default=0)

# class Player(models.Model):
#     name = models.CharField(max_length=50)
#     items = ArrayField(
#             models.CharField(max_length=50, blank=True),
#             size=100,
#         )
#     description = models.CharField(max_length=500)
#     health_points = models.FloatField()
#     lives = models.IntegerField(default=3)
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
