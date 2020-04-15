from rest_framework import serializers

from api.utilities.models import Utility


class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ('houseId', 'name', 'isBookable')
