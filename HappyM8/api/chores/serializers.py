from rest_framework import serializers

from api.bookings.models import Booking
from api.houses.models import House


class ChoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('userId', 'name', 'description', 'beginTime', 'endTime')
