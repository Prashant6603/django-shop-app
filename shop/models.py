from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    category = models.CharField(max_length=100)

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

