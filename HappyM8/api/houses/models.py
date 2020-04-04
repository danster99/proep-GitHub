from django.db import models
from api.users.models import User
# Create your models here.


class House(models.Model):
    address = models.CharField(max_length=400)
    max_nr_tenants = models.IntegerField()
    rules = models.FileField()
    tenants = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Room(models.Model):
    room_type = models.CharField(max_length=50)
    is_bookable = models.BooleanField(default=True)
    house_id = models.ForeignKey(Houseon_delete=models.CASCADE, default=0)
