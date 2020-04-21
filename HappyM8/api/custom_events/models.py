from django.db import models
from api.users.models import User


# Create your models here.


class CustomEvent(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notify_admin = models.BooleanField(default=False)
