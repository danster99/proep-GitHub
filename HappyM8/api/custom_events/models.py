from django.db import models
from api.users.models import User


# Create your models here.


class CustomEvent(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    beginTime = models.DateTimeField()
    endTime = models.DateTimeField()
    notifyAdmin = models.BooleanField(default=False)
