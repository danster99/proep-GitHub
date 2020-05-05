from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from api.users.models import User, Tenant
from api.users.serializers import UserSerializer,  TenantSerializer,\
    TenantSerializerCode
from rest_framework.mixins import CreateModelMixin


class UserList(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve existing clients. It is possible to filter clients by email.
        ex: ?email='some-client@mail.com'
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().retrieve(request, *args, **kwargs)

    # @action(detail=False, methods=['get'], url_path='detail')
    # def getUserByEmail(self, request):
    #     """
    #     get user by email
    #     :param request:
    #     :return:
    #     """
    #     user = get_object_or_404(User, email__exact=request.query_params.get('email'))
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    #     # tenant = get_object_or_404(Tenant,email__exact=request.data.get('email'))
    #     # serializer = TenantSerializerCode(tenant)
    #     # return Response(serializer.data)


class TenantList(GenericViewSet, CreateModelMixin):

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    def perform_create(self, serializer):
        house = serializer.validated_data.get('house')
        current_tenants = Tenant.objects.filter(house=house)
        if house.max_nr_tenants > current_tenants.count():
            return serializer.save()

    def create(self, request, *args, **kwargs):
        """
        Create a new tenant
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path='code')
    def get_tenant_code(self, request):
        """
        So if a method is not defined in an action,
         it will automatically create all endpoints for CRUD
        :param request:
        :return:
        """
        tenant = get_object_or_404(Tenant, email__exact=request.query_params.get('email'))
        serializer = TenantSerializerCode(tenant)
        return Response(serializer.data)

    @action(detail=False, url_path='update/status', methods=['put'])
    def update_tenant_status(self, request, *args, **kwargs):
        tenant = get_object_or_404(Tenant, email__exact=request.query_params.get('email'))
        serializer = TenantSerializer(tenant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     """
    #     Assign make user a tenant, change status to assigned
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     return super().update(request, *args, **kwargs)
    #
    # def perform_update(self, serializer):
    #     instance = self.get_object()
    #     instance.user_id = serializer.data.get("user")
    #     instance.status = 2
    #     instance.save()
    #     super().perform_update(serializer)
