from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db.models import Model


class Flights(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    flightId = models.CharField(max_length=200)
    flightName = models.CharField(max_length=200)
    From = models.CharField(max_length=200)
    To = models.CharField(max_length=300)
    departure_time = models.DateTimeField(auto_now_add=True)
    expected_arrival_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    airline = models.CharField(max_length=200, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)


class FlightBookings(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=40)
    confirmationID = models.CharField(max_length=40)
    flightName = models.CharField(max_length=40)
    flightCompany = models.CharField(max_length=40)
    DepartureAirport = models.CharField(max_length=40)
    ArrivalAirport = models.CharField(max_length=40)

    providerConfirmationId = models.CharField(max_length=40)
    DepartureTime = models.DateTimeField(auto_now_add=True)
    ArrivalTime = models.DateTimeField(auto_now_add=True)
    traveler = models.CharField(max_length=40)
    Price = models.CharField(max_length=40)
    currency = models.CharField(max_length=10, null=True)
    offerid = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "FlightBooking"

class flight_bookings(models.Model):
    pass
