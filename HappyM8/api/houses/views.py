from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.houses.models import House
from api.houses.serializers import HouseSerializer


class HouseList(APIView):
    def get(self, format=None):
        houses = House.objects.all
        serializer = HouseSerializer(houses)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
