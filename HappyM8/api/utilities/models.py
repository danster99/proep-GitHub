from django.db import models
from api.houses.models import House


# Create your models here.


class Utility(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
