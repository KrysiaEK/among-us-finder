from django.db import models


class Room(models.Model):
    LEVEL_CHOICES = [(1, 'Beginner'), (2, 'Medium'), (3, 'Advanced')]
    MAP_CHOICES = [(1, 'The Skeld'), (2, 'Polus'), (3, 'MiraHQ'), (4, 'The Airship')]
    PLAYERS_NUMBER = [(4, "4"), (5, "5"), (6, "6"), (7, '7'), (8, "8"), (9, "9"), (10, "10")]
    SEARCHED_PLAYERS_NUMBER = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, '7'), (8, "8"), (9, "9")]
    name = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    time = models.TimeField()
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    map = models.PositiveSmallIntegerField(choices=MAP_CHOICES)
    players_number = models.PositiveSmallIntegerField(choices=PLAYERS_NUMBER)
    searched_players_number = models.PositiveSmallIntegerField(choices=SEARCHED_PLAYERS_NUMBER)
    comment = models.TextField(blank=True)
