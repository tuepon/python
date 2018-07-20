from django.db import models
from django.utils import timezone


class Account(models.Model):
    aim = models.IntegerField('設定金額')
    date = models.DateTimeField(default=timezone.now)

# Create your models here.
