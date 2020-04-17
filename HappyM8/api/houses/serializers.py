from rest_framework import serializers
from api.houses.models import House, Room
from api.users.serializers import UserSerializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_type', 'is_bookable')


class HouseSerializer(serializers.ModelSerializer):

    room_set = RoomSerializer(many=True, read_only=True)
    tenant = UserSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField()

    class Meta:
        model = House
        fields = ('address',  'max_nr_tenants', 'rules',
                  'owner', 'room_set', 'tenant')
