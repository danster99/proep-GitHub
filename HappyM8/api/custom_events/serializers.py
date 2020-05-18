from rest_framework import serializers
from api.custom_events.models import CustomEvent


class CustomEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomEvent
        fields = ('user', 'name', 'description',
                  'begin_time', 'end_time', 'house')
