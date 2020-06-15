from django.db import models
from api.users.views import User
from api.houses.models import House


class Chore(models.Model):

    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    begin_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    # foreign keys
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
