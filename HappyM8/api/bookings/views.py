from rest_framework.viewsets import ModelViewSet

from api.bookings.models import Booking
from api.bookings.serializers import BookingSerializer


class BookingList(ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieve existing bookings
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create a new booking
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """
        Checks if the
        :param serializer:
        :return:
        """
