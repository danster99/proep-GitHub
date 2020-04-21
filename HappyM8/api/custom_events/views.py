from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from api.custom_events.models import CustomEvent
from api.custom_events.serializers import CustomEventSerializer


class CustomEventList(ModelViewSet):

    queryset = CustomEvent.objects.all()
    serializer_class = CustomEventSerializer

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

    def create(self, request, *args, **kwargs):
        """
        Create a new custom event
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)