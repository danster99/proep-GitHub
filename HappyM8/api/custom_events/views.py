from rest_framework.viewsets import ModelViewSet
from api.custom_events.models import CustomEvent
from api.custom_events.serializers import CustomEventSerializer
from api.custom_events.filters import CustomFilter


class CustomEventList(ModelViewSet):

    queryset = CustomEvent.objects.all()
    serializer_class = CustomEventSerializer
    filter_backends = [CustomFilter, ]

    def list(self, request, *args, **kwargs):
        """
        Retrieve list of custom events
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
        """
        alter creation of custom event to difference bewteen a tenant and a
        landlord creating the event
        also stores the house the event belongs to
        :param serializer:
        :return:
        """
        if self.request.user.is_admin:
            return serializer.save(user=self.request.user,
                               house=self.request.user.tenant.house,
                                   from_admin=True, notify_owner=False)
        else:
            return serializer.save(user=self.request.user,
                                   from_admin=False)