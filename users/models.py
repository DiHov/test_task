from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.CharField(unique=True, primary_key=True, max_length=120)
    username = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = [
        'password',
    ]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.id


class Ping(object):
    def __init__(self, latency):
        self.latency = latency
