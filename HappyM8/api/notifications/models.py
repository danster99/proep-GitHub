from django.db import models
from api.users.models import User
from api.houses.models import House


class Notification(models.Model):

    description = models.TextField(max_length=200)

    # foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
