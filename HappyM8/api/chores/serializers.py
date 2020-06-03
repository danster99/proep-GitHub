from rest_framework import serializers
from api.chores.models import Chore
from api.users.serializers import UserSerializer


class ChoreSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField()

    class Meta:
        model = Chore
        fields = ('id', 'name', 'user', 'begin_time', 'end_time', 'description')


class NewChoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chore
        fields = ('id', 'name', 'description', 'house')


class ChoreCalendar(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Chore
        fields = ('name', 'user', 'begin_time', 'end_time', 'description')