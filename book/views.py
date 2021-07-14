import json
import ast
from amadeus import Client, ResponseError, Location
from django.shortcuts import render
from django.contrib import messages
from sendgrid import Mail, SendGridAPIClient
from sendgrid.helpers.mail import email

from . import flight
from .flight import Flight
from .booking import Booking
from django.http import HttpResponse
from .models import FlightBookings, Flights

#
# amadeus production
amadeus = Client(
        client_id='itAu7wJi164TVE1xgGnQ1hDTnnL7jchA',
        client_secret='3LlE97fVMg7AaWqG',
        hostname='test'
    )


# amadeus = Client(
#     client_id='3MCFjLGhW3lJwBJtdAMirNGkc8FUoL4s',
#     client_secret='OJEffyNYNtbPandi',
#     hostname='test',
#
# )


def book(request):
    origin = request.POST.get('Origin')
    destination = request.POST.get('Destination')
    departureDate = request.POST.get('Departuredate')
    returnDate = request.POST.get('Returndate')
    adults = request.POST.get('Adults')

    if not adults:
        adults = 1

    kwargs = {'originLocationCode': origin,
              'destinationLocationCode': destination,
              'departureDate': departureDate,
              'adults': adults
              }

    tripPurpose = ''
    if returnDate:
        kwargs['returnDate'] = returnDate
        try:
            trip_purpose_response = amadeus.travel.predictions.trip_purpose.get(**kwargs).data

            tripPurpose = trip_purpose_response['result']

        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
            return render(request, 'book/flights.html', {})

    if origin and destination and departureDate:
        try:
            flight_offers = amadeus.shopping.flight_offers_search.get(**kwargs)

            prediction_flights = amadeus.shopping.flight_offers.prediction.post(flight_offers.result)


        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
            return render(request, 'book/flights.html', {})

        flights_offers_returned = []

        for flight in flight_offers.data:
            # print(flight['id'],'fffffffffffffffffffffffffff')

            offer = Flight(flight).construct_flights()  # creating the object offer of the Flight class
            offer['flight'] = flight
            flights_offers_returned.append(offer)

        prediction_flights_returned = []

        for flight in prediction_flights.data:
            offer = Flight(flight).construct_flights()

            flightid = flight['id']
            # print('flightid', flightid, '---------------------------------------------------')

            prediction_flights_returned.append(offer)
            prediction_flights_returned.append(flight)

            # print(prediction_flights_returned, '999999999999999999999999999', flightId)

            context = {'response': flights_offers_returned,
                       # 'prediction': prediction_flights_returned,
                       'origin': origin,

                       'destination': destination,
                       'departureDate': departureDate,
                       'returnDate': returnDate,
                       'tripPurpose': tripPurpose,
                       'adults': adults,
                       'flightid': flightid,
                       'flight': flight,

                       }

        return render(request, 'book/flights.html', context)

    return render(request, 'book/flights.html', {})


def viewDetails(request, flightid):
    if request.method == 'POST':
        offer = request.POST.get('offer')
        # flight = request.POST.get('flight')
        offer = eval(offer)
        # ourflight = eval(flight)
        # print('fliggggggggggggggggggggggggggkkkkkkkkkkkkkkkkkkkkkkkkkkgghttttttttt', ourflight)

        context = {

            'flightid': flightid,
            'offer': offer,
            # 'flight': flight,

        }

        return render(request, 'book/bookFlight.html', context)

    else:
        return HttpResponse("you seem lost")


def flightChekout(request, flightid):
    if request.method == 'POST':
        offer = request.POST.get('offer')
        # flight = request.POST.get('flight')
        offer = eval(offer)
        # flight = eval(flight)

        context = {
            'flightid': flightid,
            'offer': offer,
            # 'flight': flight,

        }

        return render(request, 'book/bookFlightCheckout.html', context)


def origin_airport_search(request):
    if request.is_ajax():
        try:
            data = amadeus.reference_data.locations.get(keyword=request.GET.get('term', None),
                                                        subType=Location.ANY).data
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
    return HttpResponse(get_city_airport_list(data), 'application/json')


def destination_airport_search(request):
    if request.is_ajax():
        try:
            data = amadeus.reference_data.locations.get(keyword=request.GET.get('term', None),
                                                        subType=Location.ANY).data
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
    return HttpResponse(get_city_airport_list(data), 'application/json')


def get_city_airport_list(data):
    result = []
    for i, val in enumerate(data):
        result.append(data[i]['iataCode'] + ', ' + data[i]['name'])
    result = list(dict.fromkeys(result))
    return json.dumps(result)


def book_flight(request, flightid):
    # print('---------------------------flight booking-----------------------------------')

    if request.method == 'POST':
        offer = request.POST.get('offer')
        offer = eval(offer)
        # print(offer)
        flight = offer['flight']

        dateOfBirth = request.POST.get('dateOfBirth')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        gender = request.POST.get('gender')
        emailAddress = request.POST.get('emailAddress')
        deviceType = request.POST.get('deviceType')
        countryCallingCode = request.POST.get('countryCallingCode')
        phonenumber = request.POST.get('phonenumber')
        documentType = request.POST.get('documentType')
        birthPlace = request.POST.get('birthPlace')
        issuanceLocation = request.POST.get('issuanceLocation')
        issuanceDate = request.POST.get('issuanceDate')
        number = request.POST.get('number')
        expiryDate = request.POST.get('expiryDate')
        issuanceCountry = request.POST.get('issuanceCountry')
        validityCountry = request.POST.get('validityCountry')
        nationality = request.POST.get('nationality')
        holder = request.POST.get('holder')

        print('---------------------details----------------------------')

        print(dateOfBirth, firstName, lastName, gender, emailAddress, deviceType, countryCallingCode,
              phonenumber, documentType, birthPlace, issuanceLocation, issuanceDate,
              number, expiryDate, issuanceCountry, validityCountry, nationality,
              holder, '8888888888888888888888888888888888888888888')
        # print(offer, '------------------------')

        traveler = {
            "id": "1",
            "dateOfBirth": dateOfBirth,
            "name": {"firstName": firstName, "lastName": lastName},
            "gender": gender,
            "contact": {
                "emailAddress": emailAddress,
                "phones": [
                    {
                        "deviceType": deviceType,
                        "countryCallingCode": countryCallingCode,
                        "number": phonenumber,
                    }
                ],
            },
            "documents": [
                {
                    "documentType": documentType,
                    "birthPlace": birthPlace,
                    "issuanceLocation": issuanceLocation,
                    "issuanceDate": issuanceDate,
                    "number": number,
                    "expiryDate": expiryDate,
                    "issuanceCountry": issuanceCountry,
                    "validityCountry": validityCountry,
                    "nationality": nationality,
                    "holder": holder,
                }
            ],
        }

        # Use Flight Create Orders to perform the booking
        # print(traveler,'tttttttttttttttttttttttttttttttttttttttttttt')
        try:

            # print('order here for flight ')
            # flight_price_confirmed = amadeus.shopping.flight_offers.pricing.post(flight).data#["flightOffers"]
            # price_confirm = amadeus.shopping.flight_offers.pricing.post(flight).data
            price_confirm = amadeus.shopping.flight_offers.pricing.post(flight).data["flightOffers"]
            # price_confirm = amadeus.shopping.flight_offers.pricing.post(
            #     ast.literal_eval("flight")
            # ).data["flightOffers"]
            # print(price_confirm, '777777777777777777777777777777')
            # order = amadeus.booking.flight_orders.post(flight_price_confirmed, traveler).data
            # print(order,'ooooooooooooooooooooooooooooooooooorder')


        except ResponseError as error:
            print(error)

            messages.add_message(request, messages.ERROR, error.response.body)

            context = {

                'flightid': flightid,

                'emailAddress': emailAddress,
                'offer': offer,

                'firstName': firstName,
            }
            return render(request, "book/flightConfirmation.html", context)

            # Use Flight Create Orders to perform the booking

        try:
            order = amadeus.booking.flight_orders.post(price_confirm, traveler).data

            # print(traveler, '0000000000000000000000000000000')
            # print(order)
            confirmId = order['id']
            reference = order['associatedRecords'][0]['reference']

            context = {

                'flightid': flightid,
                'emailAddress': emailAddress,
                'offer': offer,
                'confirmId': confirmId,
                'reference': reference,

                'firstName': firstName,
                'lastName': lastName,
                # 'offerid':offerid,

            }

            passenger_name_record = []
            booking = Booking(order).construct_booking()
            passenger_name_record.append(booking)

            flightBooking = FlightBookings(first_name=firstName, last_name=lastName, email=emailAddress,
                                           confirmationID=confirmId,
                                           offerid=reference, phone=phonenumber)

            flightBooking.save()

            ms = '''

                     <h1> Your flight booking journey was successfull.</h1>
                     <h3> Hello {firstname},</h3>
                     <br>Your booking Confirmation Id is : {confirmationID}.</br>

                     '''
            message = Mail(
                from_email='info@sky-swift.com',
                to_emails=emailAddress,
                subject='Flight  Booking Confirmation',
                html_content=ms,

            )

            try:
                sg = SendGridAPIClient('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')
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)

            except Exception as e:
                print('So sorry an error occurred', e)

            return render(request, "book/flightConfirmation.html", context)


        except ResponseError as error:
            messages.add_message(
                request, messages.ERROR, error.response.result["errors"][0]["detail"]
            )

            return render(request, "book/flightConfirmation.html", {})

        # sending flight booking mail

    # context = {
    #
    #     'flightid': flightid,
    #     "response": passenger_name_record,
    #     'firstName': firstName,
    # }
    #
    #     return render(request, "book/flightConfirmation.html", context)
