from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from api.utilities.models import Utility
from api.utilities.serializers import UtilitySerializer


class UtilityList(ModelViewSet):

    queryset = Utility.objects.all()
    serializer_class = UtilitySerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieve existing clients. It is possible to filter clients by email.
        ex: ?email='some-client@mail.com'
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

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

    @action(detail='true', methods=['[post]'], url_path='houses')
    def post(self, request, format=None):
        serializer = UtilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
