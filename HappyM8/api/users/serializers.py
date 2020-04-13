from rest_framework import serializers
from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ('first_name', 'last_name', 'email', 'password', 'is_admin')

