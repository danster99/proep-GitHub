from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from api.users.models import User, Tenant
from api.users.serializers import UserSerializer, TenantSerializer,\
    TenantSerializerCode, TenantSerializerUser
from rest_framework.mixins import CreateModelMixin
from api.houses.models import House

class UserList(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

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


class TenantList(GenericViewSet, CreateModelMixin):

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    def perform_create(self, serializer):
        instance = House.objects.get(pk=self.request.data.get('house'))
        current_tenants = Tenant.objects.filter(house=instance)
        if instance.max_nr_tenants < current_tenants.count():
            return super().perform_create(serializer)

    def create(self, request, *args, **kwargs):
        """
        Create a new tenant
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)


class TenantListCode(ReadOnlyModelViewSet):

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializerCode
    lookup_field = 'email'

    def retrieve(self, request, *args, **kwargs):
        """
        get code of a user by email
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().retrieve(request, *args, **kwargs)


class TenantListUser(GenericViewSet):

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializerUser
    lookup_field = 'email'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user = request.data.get("user")
        instance.status = 2
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
