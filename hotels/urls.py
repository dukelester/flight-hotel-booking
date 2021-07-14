from django.contrib import admin
from django.urls import path,include
from .views import search, hoteldetails, roomdetails,bookingform,book

urlpatterns = [

    path('search', search, name='searchresults'),
    path('hoteldetails/<str:hotelid>', hoteldetails, name='hoteldetails'),
    path('roomdetails/<str:offer_id>', roomdetails, name='roomdetails'),
    path('book/<str:offerid>', book, name='book'),
    path('bookingform/<str:offerid>', bookingform, name='bookingform'),
    ]