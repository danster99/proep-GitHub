from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.houses.models import House, Room
from api.houses.serializers import HouseSerializer, RoomSerializer
from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from api.houses.filters import HouseFilter
from rest_framework.viewsets import ModelViewSet


class HouseList(ModelViewSet):

    queryset = House.objects\
        .prefetch_related('room_set', 'tenant_set', 'utility_set')\
        .all()
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [HouseFilter, ]

    def update(self, request, *args, **kwargs):
        """
        update a house's details
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create house
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, *kwargs)

    @action(detail=False, methods=['get'], url_path='user')
    def get_house_for_user(self, request):
        """
        get user by email
        :param request:
        :return:
        """
        queryset = self.get_queryset()
        if not self.request.user.is_admin:
            obj = get_object_or_404(queryset, tenant__user=self.request.user)
            serializer = HouseSerializer(obj)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RoomList(GenericViewSet, CreateModelMixin):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new room
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        house = user.tenant.house
        return serializer.save(house=house)
