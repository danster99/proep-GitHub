from django.db import models
from HappyM8.houses.models import House
# Create your models here.


STATUS_PENDING = 1
STATUS_ASSIGNED = 2
STATUS_UNASSIGNED = 3


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField()
    phone_nr = models.CharField(max_length=11, null=True, blank=True)
    code = models.CharField(null=True, blank=True)
    status_choices = {
        'pending': STATUS_PENDING,
        'assigned': STATUS_ASSIGNED,
        'unassigned': STATUS_UNASSIGNED
    }
    status = models.CharField(choices=status_choices)
    is_admin = models.BooleanField(default=False)

    # Foreign key
    house_id = models.ForeignKey(House, on_delete=models.CASCADE, default=0)

    @property
    def is_pending(self):
        return self.status == STATUS_PENDING

    @property
    def is_assigned(self):
        return self.status == STATUS_ASSIGNED

    @property
    def is_unassigned(self):
        return self.status == STATUS_UNASSIGNED

    @classmethod
    def email_used(cls, email):
        filters = {'email': email.lower()}
        return cls.objects.filter(**filters).count() > 0