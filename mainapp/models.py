from django.db import models
from uuid import uuid4


# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


class Tokens(models.Model):
    token = models.CharField(max_length=36, unique=True)

    def create_token(self):
        self.token = uuid4()
        self.save()
