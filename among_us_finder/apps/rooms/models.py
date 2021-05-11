from django.db import models


class Room(models.Model):
    LEVEL_CHOICES = [(1, 'Beginner'), (2, 'Medium'), (3, 'Advanced')]
    MAP_CHOICES = [(1, 'The Skeld'), (2, 'Polus'), (3, 'MiraHQ'), (4, 'The Airship')]
    PLAYERS_NUMBER = [(4, "4"), (5, "5"), (6, "6"), (7, '7'), (8, "8"), (9, "9"), (10, "10")]
    SEARCHED_PLAYERS_NUMBER = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, '7'), (8, "8"), (9, "9")]
    name = models.CharField(max_length=20, blank=True)
    game_start = models.DateTimeField()
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    map = models.PositiveSmallIntegerField(choices=MAP_CHOICES, null=True, blank=True)
    players_number = models.PositiveSmallIntegerField(choices=PLAYERS_NUMBER)
    searched_players_number = models.PositiveSmallIntegerField(choices=SEARCHED_PLAYERS_NUMBER)
    comment = models.TextField(blank=True)
    participants = models.ManyToManyField('users.User')
    host = models.ForeignKey('users.User', blank=False, null=True, on_delete=models.SET_NULL, related_name='host')


class Message(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
