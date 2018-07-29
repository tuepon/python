from django.db import models
from django.utils import timezone

class Aim(models.Model):
#   amount = models.IntegerField('設定金額', default='')
    amount = 600000

class Deposit(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    sent = models.IntegerField('入金額', default='')
    balance = models.IntegerField('残高', default='')


