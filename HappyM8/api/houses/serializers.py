from rest_framework import serializers
from api.houses.models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('address', 'max_nr_tenants', 'rules')


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('room_type', 'is_bookable', 'house_id')
