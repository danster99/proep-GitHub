from rest_framework import serializers

from api.bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('user', 'room', 'description', 'begin_time', 'end_time')
