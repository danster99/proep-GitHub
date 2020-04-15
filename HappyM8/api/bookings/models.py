from django.db import models
# Create your models here.
from api.houses.models import Room
from api.users.models import User
#from api.chores.models import Utility


class Booking(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE)
    #utilityId = models.ForeignKey(Utility, on_delete = models.CASCADE)
    description = models.TextField(max_length=500)
    beginTime = models.DateTimeField()
    endTime = models.DateTimeField()

