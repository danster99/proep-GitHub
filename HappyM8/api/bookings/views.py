from rest_framework.viewsets import GenericViewSet
from api.bookings.models import Booking
from api.bookings.serializers import BookingSerializer
from rest_framework.serializers import ValidationError
from api.bookings.filters import BookingFilter
from rest_framework.mixins import CreateModelMixin


class BookingList(CreateModelMixin, GenericViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [BookingFilter, ]

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
        performs the creation of a booking with preexisting conditions
        Checks if:
            One of the times provided is incorrect:
                Start time interferes with another event
                End time interferes with another event
            Both times provided are incorrect:
                Event is in the exact same time as another event
                For an event that starts after an existing event and ends before it
                For an event which starts before an existing one and ends after it
        adds the house of the tenant who created the task (who is currently logged in)
        adds as creator the currently logged in user
        :param serializer:
        :return:
        """
        start_time = serializer.validated_data.get('begin_time')
        finish_time = serializer.validated_data.get('end_time')
        room = serializer.validated_data.get('room')
        utility = serializer.validated_data.get('utility')
        bookings = Booking.objects.filter(utility=utility, room=room)
        if not bookings:
            return serializer.save(user=self.request.user,
                                   house=self.request.user.tenant.house)
        for booking in bookings:
            if booking.begin_time == start_time and booking.end_time == finish_time:
                raise ValidationError("begin or end time overlap")
            elif booking.begin_time < start_time < booking.end_time:
                raise ValidationError("begin time overlaps")
            elif booking.begin_time < finish_time < booking.end_time:
                raise ValidationError("end time overlaps")
            elif start_time > booking.begin_time > finish_time and start_time > booking.end_time >finish_time:
                raise ValidationError("overlap")
            else:
                return serializer.save(user=self.request.user,
                                       house=self.request.user.tenant.house)
