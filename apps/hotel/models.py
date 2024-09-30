from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Amenity(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.name

class RoomTier(models.Model):
    ROOM_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ]
    

    title = models.CharField(max_length= 50)
    room_type = models.CharField( verbose_name = _('Room Size'), max_length=15, choices=ROOM_CHOICES)
    description = models.CharField(max_length = 500, verbose_name = _('Description'))
    available_rooms = models.IntegerField( verbose_name = _('Available Rooms'))
    price = models.IntegerField()
    Amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.title


class Booking(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    roomtier = models.ForeignKey(RoomTier, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Total Price'))
    def __str__(self):
        return f"{self.roomtier.title} is booked for {self.firstname} {self.lastname} from {self.check_in} to {self.check_out}"

class RoomRating(models.Model):
    roomtier = models.ForeignKey(RoomTier, verbose_name = _('Room Tier'), on_delete = models.CASCADE)
    rating = models.IntegerField( verbose_name = _('Rating'))

