
from rest_framework.viewsets import ModelViewSet

from api.houses.models import House, Room
from api.houses.serializers import HouseSerializer, RoomSerializer
from rest_framework import permissions
from api.houses.filters import IsOwnerFilter


class HouseList(ModelViewSet):

    queryset = House.objects\
        .prefetch_related('room_set', 'tenant_set', 'utility_set')\
        .all()
    serializer_class = HouseSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = IsOwnerFilter

    def create(self, request, *args, **kwargs):
        """
        Create house
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, *kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve existing houses. It is possible to filter houses by address.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().retrieve(request, *args, **kwargs)
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class RoomList(ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Create a new room
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Get a specific room
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().retrieve(request, *args, **kwargs)
