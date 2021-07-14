from django.contrib import admin

# from .views import flightBooking
from .models import Flights, FlightBookings

# Register your models here.

admin.site.register(Flights)
admin.site.register(FlightBookings)


#
#
# class BookedFlights(admin.ModelAdmin):
#     model = Flights
#     list_display = "__all__"
#
#     def get_name(self, obj):
#         return obj.F.name
#
#     get_name.admin_order_field = 'flightName'  # Allows column order sorting
#     get_name.short_description = 'airline'  # Renames column head
#
#     # Filtering on side - for some reason, this works
    # list_filter = ['flightName', 'flightId', 'From', 'To']


