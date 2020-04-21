from rest_framework import serializers
from api.users.models import User
from api.users.models import Tenant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class TenantSerializer(serializers.ModelSerializer):
    """
    Used for post
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Tenant
        fields = ('code', 'email', 'house', 'user')


class TenantSerializerCode(serializers.ModelSerializer):
    """
    used for getting the code
    """
    class Meta:
        model = Tenant
        fields = ('code', 'email')
        lookup_field = 'email'


class TenantSerializerUser(serializers.ModelSerializer):

    email = serializers.ReadOnlyField()

    class Meta:
        model = Tenant
        fields = ('user', 'status', 'email')
        lookup_field = 'email'
