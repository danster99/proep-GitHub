from rest_framework.viewsets import ModelViewSet
from api.notifications.models import Notification
from api.notifications.serializers import NotificationSerializer
from api.notifications.filters import NotificationFilter


class NotificationList(ModelViewSet):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [NotificationFilter, ]

    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of notifications with name and description
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        create a new notification
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """
        save the detalils of the logged in user as creator and the house they
        are assigned to as reference
        :param serializer:
        :return:
        """
        user = self.request.user
        house = user.tenant.house
        return serializer.save(house=house, user=user)