
from rest_framework.viewsets import ModelViewSet

from api.chores.models import Chore
from api.chores.serializers import ChoreSerializer, NewChoreSerializer


class ChoreList(ModelViewSet):

    queryset = Chore.objects.all()
    serializer_class = ChoreSerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieve existing chores with user and assigned time.
        ex: ?email='some-client@mail.com'
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Add user as well as begin and end time for an existing chore
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().update(request, *args, **kwargs)


class NewChoreList(ModelViewSet):

    queryset = Chore.objects.all()
    serializer_class = NewChoreSerializer

    def list(self, request, *args, **kwargs):
        """
        get chores with name and description
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        create a new chore
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)
