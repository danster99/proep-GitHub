from rest_framework import serializers
from api.users.serializers import UserSerializer
from api.bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('user', 'room', 'utility', 'description', 'begin_time',
                  'end_time')


class BookingCalendar(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    room = serializers.SlugRelatedField(read_only=True, slug_field='room_type')
    utility = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Booking
        fields = ('user', 'room', 'utility', 'description', 'begin_time',
                  'end_time')