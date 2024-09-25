from rest_framework import serializers
from .models import RoomTier, RoomRating

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomTier
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomRating
        fields = '__all__'