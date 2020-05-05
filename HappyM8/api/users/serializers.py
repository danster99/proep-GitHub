from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from api.users.models import User
from api.users.models import Tenant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.CharField()
    is_admin = serializers.BooleanField()

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'age': self.validated_data.get('age', ''),
            'is_admin': self.validated_data.get('is_admin', '')

        }

    def save(self, request):
        user = super().save(request)
        user.age = self.data.get('age')
        user.is_admin = self.data.get('is_admin')
        user.save()
        return user


class TenantSerializer(serializers.ModelSerializer):
    """
    Used for post
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Tenant
        fields = ('code', 'email', 'house', 'user', 'status')


class TenantSerializerCode(serializers.ModelSerializer):
    """
    used for getting the code
    """
    class Meta:
        model = Tenant
        fields = 'code'


class TenantSerializerUser(serializers.ModelSerializer):

    email = serializers.ReadOnlyField()

    class Meta:
        model = Tenant
        fields = ('user', 'email')

