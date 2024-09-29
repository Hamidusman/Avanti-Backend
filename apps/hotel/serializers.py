from rest_framework import serializers
from .models import RoomTier, RoomRating, Amenity, Booking
from datetime import datetime


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomTier
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['firstname', 'lastname',
                  'email', 'roomtier',
                  'check_in', 'check_out',
                  'total_price']
        read_only_fields = ['total_price']
        
    def create(self, validated_data):
        check_in = validated_data.get('check_in')
        check_out = validated_data.get('check_out')
        roomtier = validated_data.get('roomtier')

        # Calculate the total number of days
        days = (check_out - check_in).days
        if days <= 0:
            raise serializers.ValidationError("Check-out date must be after check-in date.")

        # Calculate the total price based on room price and number of days
        total_price = roomtier.price * days

        # Store total_price in the validated_data before saving the object
        validated_data['total_price'] = total_price

        # Create and return the booking
        return super().create(validated_data)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomRating
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'