from rest_framework import serializers
from api.houses.models import House, Room
from api.users.serializers import TenantSerializer
from api.utilities.serializers import UtilitySerializer
from api.notifications.serializers import NotificationSerializer


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
        fields = ('id', 'house_nr', 'postcode',  'max_nr_tenants', 'rules',
                  'owner', 'room_set', 'tenant_set', 'utility_set', 'notification_set')

