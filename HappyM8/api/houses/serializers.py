from rest_framework import serializers
from api.houses.models import House, Room
from api.users.serializers import TenantSerializer
from api.utilities.serializers import UtilitySerializer


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('room_type', 'is_bookable', 'house')


class HouseSerializer(serializers.ModelSerializer):

    room_set = RoomSerializer(many=True, read_only=True)
    tenant_set = TenantSerializer(many=True, read_only=True)
    utility_set = UtilitySerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = ('address',  'max_nr_tenants', 'rules',
                  'owner', 'room_set', 'tenant_set', 'utility_set')
