from django.shortcuts import render
from .serializers import HotelSerializers, RatingSerializer
from .models import RoomTier, RoomRating
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

# Create your views here.

class HotelView(generics.ListCreateAPIView):
    queryset =RoomTier.objects.all()
    serializer_class = HotelSerializers

class HotelDetail(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = RoomTier.objects.all()
    serializer_class = HotelSerializers


class RatingView(generics.ListCreateAPIView):
    queryset = RoomRating.objects.all()
    serializer_class = RatingSerializer

'''class RatingDetail(generics.RetrieveUpdateAPIView):
    
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = RoomRating.objects.all()
    serializer_class = RatingSerializer
'''