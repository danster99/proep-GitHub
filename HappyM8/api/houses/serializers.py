from django.db.models import Prefetch
from rest_framework import serializers
from api.houses.models import House


class HouseSerializer(serializers.ModelSerializer):
    model = House
    fields = ('address', 'max_nr_tenants', 'rules', 'tenants')


class RoomSerializers(serializers.ModelSerializer):
    model = House
    fields = ('room_type', 'is_bookable', 'house_id')
