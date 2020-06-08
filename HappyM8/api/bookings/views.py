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
        Checks if the item is available
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
