from django.contrib import admin
from .models import RoomTier, RoomRating, Booking, Amenities
# Register your models here.

admin.site.register(RoomTier)
admin.site.register(RoomRating)
admin.site.register(Booking)
admin.site.register(Amenities)