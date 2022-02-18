from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from among_us_finder.apps.rooms.constants import MapChoices, LevelChoices


class Room(models.Model):
    name = models.CharField(max_length=20, blank=True)
    game_start = models.DateTimeField()
    level = models.PositiveSmallIntegerField(choices=LevelChoices.Choices)
    game_map = models.PositiveSmallIntegerField(choices=MapChoices.Choices, null=True, blank=True)
    players_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(4), MaxValueValidator(15)])
    searched_players_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(14)])
    comment = models.TextField(blank=True)
    participants = models.ManyToManyField('users.User')
    host = models.ForeignKey('users.User', blank=False, null=True, on_delete=models.SET_NULL, related_name='host')


class Message(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
