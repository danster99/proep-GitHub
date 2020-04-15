from rest_framework import serializers
from api.houses.models import House, Room
from api.users.serializers import  UserSerializer


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ('address', 'house_owner', 'max_nr_tenants', 'rules', 'tenants')

    def get_tenants(self, instance):
        """
        Retrieve all tenants linked to a house.
        :param instance:
        :return:
        """
        tenant = House.objects \
            .prefetch_related('house_tenant_set') \
            .filter(pk=instance)
        return UserSerializer(instance=tenant, many=True).data

    def get_owner(self, instance):
        tenant = House.objects \
            .select_related('house_owner') \
            .filter(pk=instance)
        return UserSerializer(instance=tenant, many=True).data


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_type', 'is_bookable', 'house_id')
