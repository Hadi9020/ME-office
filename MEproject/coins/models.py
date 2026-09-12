from django.db import models
from members.models import Member

class Coin(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    coin_btc = models.IntegerField(default=000, max_length=1000000000)
    coin_ss  = models.IntegerField(default=000, max_length=1000000)
    coin_bgc = models.IntegerField(default=000, max_length=1000000)
    coin_plc = models.IntegerField(default=000, max_length=100) 