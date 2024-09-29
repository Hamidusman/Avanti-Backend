from django.shortcuts import render
from django.db.models import Sum
from rest_framework.decorators import api_view, action
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..hotel.models import Booking, RoomTier
from .serializers import StatSerializer
# Create your views here.

@api_view(['GET'])
def get(request):
    return Response({'person': 'hamid'})

class StatView(viewsets.ViewSet):
    @action(detail=False, methods=['get'], url_path='kkk')
    def stat(self, request): 
        bookings = Booking.objects.count()
        total_rooms = RoomTier.objects.aggregate(total=Sum('available_rooms'))['total']
        
        
        total_rooms = total_rooms or 0
        data = {
            'bookings': bookings,
            'total_rooms': total_rooms,
            'pp': bookings
        }
        
        serializer = StatSerializer(data)
         
        return Response(serializer.data, status=status.HTTP_200_OK)