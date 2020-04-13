from django.db import models
# Create your models here.


class House(models.Model):
    address = models.CharField(max_length=200)
    max_nr_tenants = models.IntegerField()
    rules = models.CharField(max_length=800)
    # tenants = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Room(models.Model):
    room_type = models.CharField(max_length=50)
    is_bookable = models.BooleanField(default=True)
    house_id = models.ForeignKey(House, on_delete=models.CASCADE, default=0)
