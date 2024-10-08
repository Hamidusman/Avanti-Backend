from django.shortcuts import render, get_object_or_404
from .serializers import HotelSerializers, RatingSerializer, BookingSerializer, AmenitySerializer
from .models import RoomTier, RoomRating, Amenity, Booking
from rest_framework.views import APIView
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

# Create your views here.

class AmenityView(generics.ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

class HotelView(generics.ListCreateAPIView):
    queryset =RoomTier.objects.all()
    serializer_class = HotelSerializers

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = RoomTier.objects.all()
    serializer_class = HotelSerializers


class RatingView(generics.ListCreateAPIView):
    queryset = RoomRating.objects.all()
    serializer_class = RatingSerializer


class Book(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    lookup_field = "id"
    lookup_url_kwarg = "id"
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            return Response({
                "message": f"Congratulations! Tier {booking.roomtier.title} has been reserved in your name.",
                "total_price": f"N{booking.total_price}"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        book = self.get_queryset()
        serializer = self.get_serializer(book, many = True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




'''class RatingDetail(generics.RetrieveUpdateAPIView):
    
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = RoomRating.objects.all()
    serializer_class = RatingSerializer
'''