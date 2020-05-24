from django.db import models


class House(models.Model):

    max_nr_tenants = models.IntegerField()
    rules = models.TextField(max_length=200)
    address = models.CharField(max_length=50, null=True, blank=True)
    house_nr = models.IntegerField(null=True, blank=True)

    # foreign keys
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)


class Room(models.Model):

    room_type = models.CharField(max_length=50)
    is_bookable = models.BooleanField(default=True)

    # foreign keys
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
