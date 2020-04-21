from django.db import models
# Create your models here.
from api.houses.models import Room
from api.users.models import User
from api.utilities.models import Utility


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True,blank=True)
    utility = models.ForeignKey(Utility, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=500)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()

