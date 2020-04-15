from rest_framework import serializers

from api.custom_events.models import CustomEvent


class CustomEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomEvent
        fields = ('userId', 'name', 'description', 'beginTime', 'endTime', 'notifyAdmin')
