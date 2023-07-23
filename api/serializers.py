from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guestCanPause', 'votesToSkip')

class UpdateRoomSerializer(serializers.ModelSerializer):

    code = serializers.CharField(validators=[])

    class Meta:
        model = Room
        fields = ('guestCanPause', 'votesToSkip', 'code')