from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from api.users.models import User, Tenant
from api.users.serializers import UserSerializer, TenantSerializer


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


class TenantList(ModelViewSet):

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    lookup_field = 'email'

    def perform_create(self, serializer):
        instance = self.get_object()
        friends = Tenant.objects.filter(house=instance.house)
        if instance.house.max_nr_tenants >= friends:
            return True

    def create(self, request, *args, **kwargs):
        """
        Create a new tenant
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().update(request, *args, **kwargs)


class TenantListCode(ReadOnlyModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        """
        get code of a user by email
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().retrieve(request, *args, **kwargs)

