from django.db import models
from django.contrib.auth.models import AbstractUser

from among_us_finder.apps.rooms.constants import LevelChoices


class User(AbstractUser):
    level_of_advancement = models.PositiveSmallIntegerField(choices=LevelChoices.Choices)
