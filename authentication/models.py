from django.contrib.auth.models import AbstractUser
from django.db import models
from preferences.models import Currency


class User(AbstractUser):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='user', blank=True, null=True)

    def __str__(self):
        return self.username
    