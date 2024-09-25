from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Amenities(models.Model):
    name = models.CharField(max_length=20)

class RoomTier(models.Model):
    title = models.CharField(max_length= 50)
    bed_count = models.IntegerField( verbose_name = _('bed Count'))
    room_size = models.IntegerField( verbose_name = _('Room Size'))
    description = models.CharField(max_length = 500, verbose_name = _('Description'))
    available_rooms = models.IntegerField( verbose_name = _('Available Rooms'))
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    roomtier = models.ForeignKey(RoomTier, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.IntegerField(max_digits=10, decimal_places=2, verbose_name=_('Total Price'))

    def __str__(self):
        return f"Booking of {self.roomtier.title} by {self.firstname} {self.lastname} from {self.check_in} to {self.check_out}"

class RoomRating(models.Model):
    roomtier = models.ForeignKey(RoomTier, verbose_name = _('Room Tier'), on_delete = models.CASCADE)
    rating = models.IntegerField( verbose_name = _('Rating'))

