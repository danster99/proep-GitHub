from rest_framework.viewsets import ModelViewSet
from api.custom_events.models import CustomEvent
from api.custom_events.serializers import CustomEventSerializer
from api.custom_events.filters import CustomFilter, LandlordFilter


class CustomEventList(ModelViewSet):

    queryset = CustomEvent.objects.all()
    serializer_class = CustomEventSerializer
    filter_backends = [CustomFilter, LandlordFilter]

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

    def create(self, request, *args, **kwargs):
        """
        Create a new custom event
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user,
                               house=self.request.user.tenant.house)
