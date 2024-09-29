from rest_framework import serializers

class StatSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    description = serializers.CharField()