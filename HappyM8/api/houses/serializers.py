from rest_framework import serializers

from api.chores.models import Chore
from api.houses.models import House, Room
from api.users.serializers import TenantSerializer
from api.utilities.serializers import UtilitySerializer
from api.notifications.serializers import NotificationSerializer
from api.custom_events.serializers import CustomEventCalendar
from api.chores.serializers import ChoreCalendar
from api.bookings.serializers import BookingCalendar


class RoomSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta:
        model = Room
        fields = ('id', 'room_type', 'is_bookable', 'house')


class HouseSerializer(serializers.ModelSerializer):

    room_set = RoomSerializer(many=True, read_only=True)
    tenant_set = TenantSerializer(many=True, read_only=True)
    utility_set = UtilitySerializer(many=True, read_only=True)
    notification_set = NotificationSerializer(many=True, read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = House
        fields = ('id', 'house_nr', 'address',  'max_nr_tenants', 'rules',
                  'owner', 'room_set', 'tenant_set', 'utility_set', 'notification_set')


class CalendarSerializer(serializers.ModelSerializer):

    customevent_set = CustomEventCalendar(many=True, read_only=True)
    booking_set = BookingCalendar(many=True, read_only=True)
    chore_set = serializers.SerializerMethodField('get_chores')

    def get_chores(self, house):
        qs = Chore.objects.filter(user__isnull=False, house=house)
        serializer = ChoreCalendar(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = House
        fields = ('customevent_set', 'chore_set', 'booking_set')
