from rest_framework import serializers
from api.custom_events.models import CustomEvent
from api.users.serializers import UserSerializer


class CustomEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomEvent
        fields = ('user', 'name', 'description',
                  'begin_time', 'end_time', 'house', 'notify_owner')


class CustomEventCalendar(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = CustomEvent
        fields = ('user', 'name', 'description',
                  'begin_time', 'end_time', 'house', 'notify_owner')