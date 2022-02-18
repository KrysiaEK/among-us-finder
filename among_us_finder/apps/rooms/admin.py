from django.contrib import admin

from among_us_finder.apps.rooms.models import Room, Message


@admin.register(Room)
class Room(admin.ModelAdmin):
	pass


@admin.register(Message)
class Message(admin.ModelAdmin):
	pass
