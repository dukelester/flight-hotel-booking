from django.contrib import admin
from .models import Bookings

# Register your models here.


class Booking(admin.ModelAdmin):
    list_display = ('first_name','first_name','email','phone','hotel_name','Price','currency','image','offerid','confirmationID','providerConfirmationId','Check_in','Check_out','Guests','city',)
admin.site.register(Bookings,Booking)


