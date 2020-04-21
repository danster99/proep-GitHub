from rest_framework import serializers
from api.users.models import User
from api.users.models import Tenant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class TenantSerializer(serializers.ModelSerializer):
    """
    Used for post
    """
    class Meta:
        model = Tenant
        fields = ('code', 'email', 'house')
        lookup_field = 'email'



class TenantSerializerCode(serializers.ModelSerializer):
    """
    used for getting the code
    """
    email = serializers.ReadOnlyField()

    class Meta:
        model = Tenant
        fields = ('code', 'email')
        lookup_field = 'email'
