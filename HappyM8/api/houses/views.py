from typing import Dict

from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.houses.models import House, Room
from api.houses.serializers import HouseSerializer
from rest_framework import permissions


class HouseList(ModelViewSet):

    queryset = House.objects\
        .select_related('owner')\
        .prefetch_related('room_set', 'tenant')\
        .all()
    serializer_class = HouseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # don't really meed this in the context, kept for testing only
    def list(self, request, *args, **kwargs):
        """
        Retrieve existing houses.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

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

    @action(detail=True, methods=['get'])
    def get_tenants(self, request: HttpRequest,
                     pk: int = None) -> HttpResponse:
        """
        Retrieve one house by house id and all related tenants

        :param request:
        :param pk:
        :return:
        """
        house = House.objects.get(id=pk)
        serializer = self.serializer_class(house)
        return JsonResponse(serializer.data)

    @action(detail=True, methods=['get'])
    def get_rooms(self, request: HttpRequest,
                    pk: int = None) -> HttpResponse:
        """
        Retrieve one house by house id and all related rooms

        :param request:
        :param pk:
        :return:
        """
        house = House.objects.get(id=pk)
        serializer = self.serializer_class(house)
        return JsonResponse(serializer.data)

    class RoomList(ModelViewSet):

        queryset = Room.objects.all()
        serializer_class = HouseSerializer

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