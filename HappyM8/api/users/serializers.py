from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from api.users.models import User
from api.users.models import Tenant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


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
            'birth_date': self.validated_data.get('birth_date', ''),
            'is_admin': self.validated_data.get('is_admin', '')

        }

    def save(self, request):
        user = super().save(request)
        user.birth_date = self.data.get('birth_date')
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


class TenantUserSerializer(serializers.ModelSerializer):

    code = serializers.ReadOnlyField()

    class Meta:
        model = Tenant
        fields = ('user', 'status', 'code')

