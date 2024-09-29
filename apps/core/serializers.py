from rest_framework import serializers

class StatSerializer(serializers.Serializer):
    bookings = serializers.IntegerField()
    total_rooms = serializers.IntegerField()