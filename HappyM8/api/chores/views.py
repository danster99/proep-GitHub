from rest_framework.viewsets import ModelViewSet
from api.chores.models import Chore
from api.chores.serializers import ChoreSerializer, NewChoreSerializer
from api.chores.filters import ChoreFilter


class ChoreList(ModelViewSet):

    queryset = Chore.objects.all()
    serializer_class = ChoreSerializer
    filter_backends = [ChoreFilter, ]

    def list(self, request, *args, **kwargs):
        """
        Retrieves a list of chores
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Add begin and end time for an existing chore
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        """
        automated add of the currently logged in user as assigned tenant to
        perform a chore
        :param serializer:
        :return:
        """
        return serializer.save(user=self.request.user)


class NewChoreList(ModelViewSet):

    queryset = Chore.objects.all()
    serializer_class = NewChoreSerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieves lisf of chores with name and description
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

    def perform_create(self, serializer):
        """
        Altered creation of a chore to add the currently logged in user as
        reference to the house a chore belongs to
        :param serializer:
        :return:
        """
        user = self.request.user
        house = user.tenant.house
        return serializer.save(house=house)