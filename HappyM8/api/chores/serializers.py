from rest_framework import serializers

from api.bookings.models import Booking
from api.users.serializers import UserSerializer


class ChoreSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    begin_time = serializers.ReadOnlyField()
    end_time = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = ('user', 'name', 'description', 'begin_time', 'end_time')
