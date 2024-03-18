from django.db import models


# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


class Tokens(models.Model):
    token = models.CharField(max_length=36)
