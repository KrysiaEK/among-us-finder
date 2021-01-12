from django.contrib import admin
from .models import Room


@admin.register(Room)
class Room(admin.ModelAdmin):
	pass
