from django.contrib import admin

from .models import Room, Player, Npc, FoodItem, Toys, Weapons

# Register your models here.

admin.site.register(Room)
admin.site.register(Player)
admin.site.register(Npc)
admin.site.register(FoodItem)
admin.site.register(Toys)
admin.site.register(Weapons)