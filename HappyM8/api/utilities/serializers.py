from rest_framework import serializers

from api.utilities.models import Utility
from api.houses.serializers import HouseSerializer


class UtilitySerializer(serializers.ModelSerializer):

    house = HouseSerializer()

    class Meta:
        model = Utility
        fields = ('house', 'name', 'is_bookable')
