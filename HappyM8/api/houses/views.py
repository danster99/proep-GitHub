from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from api.houses.models import House
from api.houses.serializers import HouseSerializer


class HouseList(ModelViewSet):

    queryset = House.objects.\
        prefetch_related('house_tenant_set').\
        select_related('house_owner').all()
    serializer_class = HouseSerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieve existing houses.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve existing houses. It is possible to filter houses by address.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['get'], url_path='tenants')
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

    # @action(detail='true', methods=['[post]'], url_path='houses')
    # def post(self, request, format=None):
    #     serializer = HouseSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
