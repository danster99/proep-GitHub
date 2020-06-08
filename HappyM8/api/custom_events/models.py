from django.db import models
from api.users.models import User
from api.houses.models import House


class CustomEvent(models.Model):

    # foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)

    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notify_owner = models.BooleanField(default=False)
    from_owner = models.BooleanField(default=False, null=True, blank=True)