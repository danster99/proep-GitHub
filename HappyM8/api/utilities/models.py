from django.db import models
from api.houses.models import House


# Create your models here.


class Utility(models.Model):
    houseId = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    isBookable = models.BooleanField(default=False)
