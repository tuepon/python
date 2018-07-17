from django.db import models
from django.utils import timezone


class Account(models.Model):
    aim = models.IntegerField('設定金額', max_length=10000000)
    payment = models.IntegerField('入金額', max_length=10000000)
    balance = models.IntegerField('残高', max_length=10000000)
    date = models.DateTimeField('日付', default=timezone.now)

# Create your models here.
