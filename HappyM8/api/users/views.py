from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from api.users.models import User, Tenant
from api.users.serializers import UserSerializer,  TenantSerializer,\
     TenantUserSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.serializers import ValidationError


class UserList(GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='detail')
    def get_user_by_email(self, request):
        """
        get user by email
        :param request:
        :return:
        """
        user = get_object_or_404(User, email__exact=request.query_params.get('email'))
        serializer = UserSerializer(user)
        return Response(serializer.data)


class TenantList(GenericViewSet, CreateModelMixin):

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    def perform_create(self, serializer):
        house = serializer.validated_data.get('house')
        current_tenants = Tenant.objects.filter(house=house, status=2)
        if house.max_nr_tenants > current_tenants.count():
            return serializer.save()
        else:
            raise ValidationError("max tenant number already exceeded")

    def create(self, request, *args, **kwargs):
        """
        Create a new tenant
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    @action(detail=False, url_path='update/status', methods=['put'])
    def update_tenant_status(self, request, *args, **kwargs):
        tenant = Tenant.objects.get(code=request.data.get('code'), status=1)
        serializer = TenantUserSerializer(tenant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user, status=2)
        return Response(serializer.data)
