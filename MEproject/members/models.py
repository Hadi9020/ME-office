from django.db import models
from datetime import time

class Member(models.Model):
    class MLEchoices(models.TextChoices):
        LORD    = 'LR','lord'
        KING    = 'KG','king'
        META    = 'MT','meta'
        BETA    = 'BT','beta'
        MAGICAL = 'MG','magical'
        CHILD   = 'CH','child'
    class GenderChoices(models.TextChoices):
        MALE   = 'm', 'male'
        FEMALE = 'f', 'female'
        NULL   = 'n', 'null'
    first_name    = models.CharField(max_length=10)
    last_name     = models.CharField(max_length=15)
    user_name     = models.CharField(max_length=20)
    phone         = models.CharField(max_length=11)
    email         = models.EmailField()
    birth_date    = models.DateField(default=time.now())
    register_date = models.DateField(auto_created=True,auto_now_add=True)
    mle           = models.CharField(choices=MLEchoices, max_length=9)
    gender        = models.CharField(choices=GenderChoices)
    password      = models.IntegerField()