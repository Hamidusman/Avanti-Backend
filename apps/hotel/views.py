from django.shortcuts import render, get_object_or_404
from .serializers import HotelSerializers, RatingSerializer, BookingSerializer
from .models import RoomTier, RoomRating, Booking
from rest_framework.views import APIView
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


class Book(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    lookup_field = "id"
    lookup_url_kwarg = "id"
    
    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            return Response({
                "message": f"Congratulations! Tier Solitude has been booked in your name ",
                "total_price": booking.total_price
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        book = self.get_queryset()
        serializer = self.get_serializer(book, many = True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = BookingSerializer
        return Response(serializer.data)



'''class RatingDetail(generics.RetrieveUpdateAPIView):
    
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = RoomRating.objects.all()
    serializer_class = RatingSerializer
'''