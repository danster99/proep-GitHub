from django.db import models
from api.houses.models import Room
from api.users.models import User
from api.utilities.models import Utility
from api.houses.models import House


class Booking(models.Model):

    utility = models.ForeignKey(Utility, on_delete=models.CASCADE, null=True,
                                blank=True)
    description = models.TextField(max_length=500)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True,
                             blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True,
                              blank=True)

