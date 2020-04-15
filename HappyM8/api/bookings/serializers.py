from rest_framework import serializers

from api.bookings.models import Booking
from api.houses.models import House


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('userId', 'roomId',
                  # utilityId,
                  'description', 'beginTime', 'endTime')
