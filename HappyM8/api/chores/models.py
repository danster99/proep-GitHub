from django.db import models
from api.users.views import User


# Create your models here.


class Chore(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    beginTime = models.DateTimeField()
    endTime = models.DateTimeField()
