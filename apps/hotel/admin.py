from django.contrib import admin
from .models import RoomTier, RoomRating, Booking, Amenity
# Register your models here.

admin.site.register(RoomTier)
admin.site.register(RoomRating)
admin.site.register(Booking)
admin.site.register(Amenity)