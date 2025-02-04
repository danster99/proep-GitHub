from django.db import models
from api.houses.models import House
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser


STATUS_PENDING = 1
STATUS_ASSIGNED = 2
STATUS_UNASSIGNED = 3


class User(AbstractBaseUser):
    """
    A user can be of three types:
    1. admin - can create a house
    2.tenant - can access facilities, bookings and chores of an assigned house
    3."basic" user - can be assigned to a house

    A user has three types of status:
    1. pending - the user has not yet created an account to be assigned to a house
    2.assigned - a user is part of a house
    3.unassigned - a user who is not yet part of any house

    when a user creates an account, their status is unassigned by default unless they've been
    added by an owner. In this case, the status is pending/
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, unique=True)
    password = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    USERNAME_FIELD = 'email'


class Tenant(models.Model):

    status_choices = [
        (STATUS_PENDING, 'pending'),
        (STATUS_ASSIGNED, 'assigned'),
        (STATUS_UNASSIGNED, 'unassigned')
    ]
    status = models.CharField(max_length=15, choices=status_choices, default=STATUS_PENDING)
    code = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=70, unique=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE,
                              blank=True, null=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE,
                                null=True, blank=True)


