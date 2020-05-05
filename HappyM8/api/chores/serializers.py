from rest_framework import serializers
from api.chores.models import Chore


class ChoreSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField()

    class Meta:
        model = Chore
        fields = ('id', 'name', 'user', 'begin_time', 'end_time')


class NewChoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chore
        fields = ('id', 'name', 'description')
