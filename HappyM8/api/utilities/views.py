from rest_framework.viewsets import ModelViewSet
from api.utilities.models import Utility
from api.utilities.serializers import UtilitySerializer
from api.utilities.filters import UtilityFilter


class UtilityList(ModelViewSet):

    queryset = Utility.objects.all()
    serializer_class = UtilitySerializer
    filter_backends = [UtilityFilter, ]

    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of existing utilities
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create e new utility
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)
