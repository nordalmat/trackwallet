from django.db import models
from django.contrib.auth.models import AbstractUser

from preferences.models import Currency


class User(AbstractUser):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='user', blank=True, null=True)

    def __str__(self):
        return self.username
    