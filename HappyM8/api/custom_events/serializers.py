from rest_framework import serializers

from api.custom_events.models import CustomEvent
from api.users.serializers import UserSerializer


class CustomEventSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = CustomEvent
        fields = ('user', 'name', 'description',
                  'begin_time', 'end_time', 'notify_admin')
