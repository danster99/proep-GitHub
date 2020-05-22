from rest_framework.viewsets import ModelViewSet
from api.notifications.models import Notification
from api.notifications.serializers import NotificationSerializer
from api.notifications.filters import NotificationFilter


# Create your views here.
class NotificationList(ModelViewSet):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [NotificationFilter, ]

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

    def perform_create(self, serializer):
        user = self.request.user
        house = user.tenant.house
        return serializer.save(house=house, user=user)