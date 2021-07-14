from django.urls import path

from . import views

urlpatterns = [
    path('book', views.book, name='book'),
    path('origin_airport_search/', views.origin_airport_search, name='origin_airport_search'),
    path('destination_airport_search/', views.destination_airport_search, name='destination_airport_search'),
    path('viewdetails/<int:flightid>/', views.viewDetails,name='viewflight'),
    path('checkout/<int:flightid>/', views.flightChekout,name='flightcheckout'),
    # path('flightconfirmation/<int:flightid>/', views.bookConfiramation,name='flightconfirmation'),
    path('book_flight/<int:flightid>/', views.book_flight, name='book_flight'),
]
