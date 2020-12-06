from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LEVEL_CHOICES = [(1, 'Beginner'), (2, 'Medium'), (3, 'Advanced')]
    level_of_advancement = models.CharField(choices=LEVEL_CHOICES, max_length=10)
