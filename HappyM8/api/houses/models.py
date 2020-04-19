from django.db import models
# Create your models here.


class House(models.Model):
    address = models.CharField(max_length=200)
    max_nr_tenants = models.IntegerField()
    rules = models.TextField(max_length=200)
    owner = models.OneToOneField('users.User', on_delete=models.CASCADE, null=True, blank=True)


class Room(models.Model):
    room_type = models.CharField(max_length=50)
    is_bookable = models.BooleanField(default=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
