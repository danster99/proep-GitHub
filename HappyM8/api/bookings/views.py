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
        Checks if the item is available
        :param serializer:
        :return:
        """
        start_time = serializer.validated_data.get('begin_time')
        end_time = serializer.validated_data.get('end_time')
        room = serializer.validated_data.get('room')
        utility = serializer.validated_data.get('utility')
        print('\033[34m{}\033[0m'.format(Booking.objects.filter(utility=utility, room=room)))
        for booking in Booking.objects.filter(utility=utility, room=room):
            print('\033[34m{}\033[0m'.format(booking))
            print('\033[34m{}\033[0m'.format(booking.begin_time))
            print('\033[34m{}\033[0m'.format(booking.end_time))
            print('\033[34m{}\033[0m'.format('sjkvnaerjvberiguebriu'))
            print('\033[34m{}\033[0m'.format(start_time))
            print('\033[34m{}\033[0m'.format(end_time))
            if booking.begin_time >= end_time >= booking.end_time and booking.begin_time >= start_time >= booking.end_time:
                return serializer.save()

