# Create your views here.

from amadeus import Client, ResponseError
from django.shortcuts import render, redirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import Bookings
import requests
from django.core.mail import send_mail

# Create your views here.
amadeus = Client(
        client_id='itAu7wJi164TVE1xgGnQ1hDTnnL7jchA',
        client_secret='3LlE97fVMg7AaWqG',
        hostname='test'
    )


ourlist = []


def search(request):
    ourlist.clear()
    if request.method == "POST":
        citycode = request.POST.get('citycode', )
        checkindate = request.POST.get('checkindate', )
        checkoutdate = request.POST.get('checkoutdate', )

        # print(adults,children,rooms)
        destination = citycode.split()

        destination = destination[-1]

        try:
            # Get list of Hotels by city code
            hotels_by_city = amadeus.shopping.hotel_offers.get(cityCode=destination, checkInDate=checkindate,
                                                               checkOutDate=checkoutdate)
            k = hotels_by_city.data
            # print('this is data' ,k)

        except ResponseError as error:
            print(error.description())

        else:
            hotelid = "Not Availlable"
            name = "Not Availlable"
            address = "Not Availlable"
            phone = "Not Availlable"
            fax = "Not Availlable"
            distancefromcenter = "Not Availlable"
            dunits = "Not Availlable"
            description = "Not Availlable"
            hrating = "Not Availlable"
            media = "Not Availlable"
            amenities = "Not Availlable"
            guests_adults = "Not Availlable"
            price_currency = "Not Availlable"
            price_total = "Not Availlable"
            cityname = "Not Availlable"

            for i in k:
                # print(i)
                hoteldata = i

                try:

                    hotelid = hoteldata["hotel"]['hotelId']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    name = hoteldata["hotel"]['name']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    address = hoteldata["hotel"]['address']['cityName']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    phone = hoteldata["hotel"]['contact']['phone']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    fax = hoteldata["hotel"]['contact']['fax']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    distancefromcenter = hoteldata["hotel"]['hotelDistance']['distance']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    dunits = hoteldata["hotel"]['hotelDistance']['distanceUnit']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    description = hoteldata["hotel"]['description']['text']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    hrating = hoteldata["hotel"]['rating']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    media = hoteldata["hotel"]['media'][0]['uri']

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    amenities = hoteldata["hotel"]['amenities']


                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    guests_adults = hoteldata['offers'][0]['guests']['adults']


                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    price_total = hoteldata['offers'][0]['price']['total']


                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    cityname = hoteldata["hotel"]['address']['cityName']


                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    price_currency = hoteldata['offers'][0]['price']['currency']



                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    price_total = price_total = hoteldata['offers'][0]['price']['total']


                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                amenitylist = []
                for i in amenities:
                    i = str(i)
                    i = i.lower()
                    amenity = i.replace("_", " ")

                    amenitylist.append(amenity)

                rating = {
                    'comment': 'good'
                }

                if hrating == '1':
                    rating['comment'] = 'basic'
                elif hrating == '2':

                    rating['comment'] = 'Fair'


                elif hrating == '3':
                    rating['comment'] = 'Good'

                elif hrating == '4':

                    rating['comment'] = 'Very Good'

                elif hrating == '5':
                    rating['comment'] = 'Excellent'

                rating = rating['comment']
                # totalresults = ourlist.count()

                # currency_conversion
                # try:
                #     local_currency = 'USD'
                #
                #
                #
                #     url = f'https://free.currconv.com/api/v7/convert?q=EUR_{local_currency}&compact=ultra&apiKey=43dd6947aec7594b4e71'
                #     params = {
                #
                #     }
                #
                #     r = requests.post(url, params=params)
                #
                #     print(r.status_code)
                #     print(r.json())
                #
                # except:
                #     pass

                context = {

                    'hotelid': hotelid,
                    'name': name,
                    'address': address,
                    'phone': phone,
                    'fax': fax,
                    'distancefromcenter': distancefromcenter,
                    'dunits': dunits,
                    'description': description,
                    'hrating': hrating,
                    'media': media,
                    'rating': rating,
                    'amenitylist': amenitylist,
                    # 'totalresults': totalresults,
                    'guests_adults': guests_adults,
                    'price_currency': price_currency,
                    'price_total': price_total,
                    'cityname': cityname,

                }

                ourlist.append(context)

        ourcontextdict = {
            'ourlist': ourlist

        }

        return render(request, 'searchres.html', ourcontextdict)


    else:
        return redirect('/')


hoteldetailslist = []
ammenities = []


def hoteldetails(request, hotelid):
    hoteldetailslist.clear()
    ammenities.clear()

    try:
        # Get list of offers for a specific hotel
        hotel_offers = amadeus.shopping.hotel_offers_by_hotel.get(hotelId=hotelid)
        # print('this are hotel offers',hotel_offers.data)

        k = hotel_offers.data


    except ResponseError as error:
        raise error


    else:

        if k == None:
            contextdict2 = {

            }

        else:

            offers = "Not Availlable"
            ammenitiesraw = "Not Availlable"
            media = "Not Availlable"
            cityname = "Not Availlable"
            hotelname = "Not Availlable"
            line = "Not Availlable"
            latitude = "Not Availlable"
            longitude = "Not Availlable"

            try:

                offers = k.get('offers')

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:

                ammenitiesraw = k.get('hotel', ).get('amenities', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                media = k.get('hotel', ).get('media', )[0].get('uri', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                cityname = k.get('hotel', ).get('address', ).get('cityName', )



            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                hotelname = k.get('hotel', ).get('name', )



            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                latitude = k.get('hotel', ).get('latitude', )




            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                longitude = k.get('hotel', ).get('longitude', )


            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            for i in ammenitiesraw:
                i = i.replace('_', ' ')
                ammenities.append(i)
                # print(i)

            for offer in offers:
                offer_id = "Not availlable"
                checkindate = "Not availlable"
                checkoutdate = "Not availlable"
                roomtype = "Not availlable"
                roomcategory = "Not availlable"
                beds = "Not availlable"
                bedtype = "Not availlable"
                description = "Not availlable"
                currency = "Not availlable"
                price = "Not availlable"
                guests = "Not availlable"

                try:

                    offer_id = offer.get('id', )


                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    checkindate = offer.get('checkInDate', )


                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    checkoutdate = offer.get('checkOutDate', )



                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    roomtype = offer.get('room', ).get('type', )



                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    roomcategory = offer.get('room', ).get('typeEstimated', ).get('category', ).replace('_', ' ')




                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    beds = offer.get('room', ).get('typeEstimated', ).get('beds', )




                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    bedtype = offer.get('room', ).get('typeEstimated', ).get('bedType', )



                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    description = offer.get('room', ).get('description', ).get('text', )



                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    currency = offer.get('price', ).get('currency', )



                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    price = offer.get('price', ).get('total', )

                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                try:
                    guests = offer.get('guests', ).get('adults', )




                except (KeyError, AttributeError, TypeError) as e:
                    print(e)

                context = {

                    'offer_id': offer_id,
                    'checkindate': checkindate,
                    'checkoutdate': checkoutdate,
                    'roomtype': roomtype,
                    'roomcategory': roomcategory,
                    'beds': beds,
                    'bedtype': bedtype,
                    'description': description,
                    'hotelid': hotelid,
                    'currency': currency,
                    'price': price,
                    'guests': guests,

                }

                hoteldetailslist.append(context)

            hoteldetails = k
            contextdict2 = {
                'hoteldetailslist': hoteldetailslist,
                'ammenities': ammenities,
                'media': media,
                'cityname': cityname,
                'hotelname': hotelname,
                'line': line,
                'latitude': latitude,
                'longitude': longitude,
                'hoteldetails': hoteldetails,

            }

        return render(request, 'searchItem.html', contextdict2)


hotelroom = []


def roomdetails(request, offer_id):
    if request.method == 'POST':
        hoteldetails = request.POST.get('hoteldetails')

        k = eval(hoteldetails)
        ammenitiesraw = "Not Availlable"
        media = "Not Availlable"
        cityname = "Not Availlable"
        hotelname = "Not Availlable"
        line = "Not Availlable"
        latitude = "Not Availlable"
        longitude = "Not Availlable"

        try:
            ammenitiesraw = k.get('hotel', ).get('amenities', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        try:
            media = k.get('hotel', ).get('media', )[0].get('uri', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        try:

            cityname = k.get('hotel', ).get('address', ).get('cityName', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            hotelname = k.get('hotel', ).get('name', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        try:
            line = k.get('hotel', ).get('address', ).get('lines', )[0]

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        try:
            latitude = k.get('hotel', ).get('latitude', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            longitude = k.get('hotel', ).get('longitude', )
        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        try:
            # Confirm the availability of a specific offer
            offer_availability = amadeus.shopping.hotel_offer(offer_id).get()
            # print('this is offer availlability',offer_availability.data)
            k = offer_availability.data

            myconst = k

        except ResponseError as error:

            raise error

        else:

            offerid = "Not availlable"

            citycode = "Not availlable"
            countrycode = "Not availlable"
            availability = "Not availlable"
            roomtype = "Not availlable"
            roomcat = "Not availlable"
            bed = "Not availlable"
            bedtype = "Not availlable"
            checkindate = "Not availlable"
            checkout = "Not availlable"
            boardtype = "Not availlable"
            typeestimated = "Not availlable"
            description = "Not availlable"
            guests = "Not availlable"
            currency = "Not availlable"
            base = "Not availlable"
            total = "Not availlable"
            pricevariations = "Not availlable"
            creitcards = "Not availlable"
            acceptedPaymnts = "Not availlable"
            paymenttype = "Not availlable"
            checkinout = "Not availlable"
            cancellation = "Not availlable"
            try:
                offerid = myconst.get('offers', )[0].get('id', ),
            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                citycode = myconst.get('hotel', ).get('cityCode', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                countrycode = myconst.get('hotel', ).get('address', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                availability = myconst.get('available', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                roomtype = myconst.get('offers', )[0].get('room', ).get('type', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                roomcat = myconst.get('offers', )[0].get('room', ).get('typeEstimated', ).get('category', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                bed = myconst.get('offers', )[0].get('room', ).get('typeEstimated', ).get('bedType', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                boardtype = myconst.get('offers', )[0].get('boardType', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                checkindate = myconst.get('offers', )[0].get('checkInDate', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                checkout = myconst.get('offers', )[0].get('checkOutDate', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                typeestimated = myconst.get('offers', )[0].get('room', ).get('typeEstimated', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                description = myconst.get('offers', )[0].get('room', ).get('description', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                guests = myconst.get('offers', )[0].get('guests', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                currency = myconst.get('offers', )[0].get('price', ).get('currency', ),

            except (KeyError, AttributeError, TypeError) as e:

                print(e)
            try:
                base = myconst.get('offers', )[0].get('price', ).get('base', ),
            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                total = myconst.get('offers', )[0].get('price', ).get('total', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                pricevariations = myconst.get('offers', )[0].get('price', ).get('variations', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                bedtype = myconst.get('offers', )[0].get('room', ).get('typeEstimated', ).get('bedType', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                creitcards = myconst.get('offers', )[0].get('policies', ).get('guarantee', ).get(
                    'acceptedPayments', ).get('creditCards', ),


            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                acceptedPaymnts = myconst.get('offers', )[0].get('policies', ).get('guarantee', ).get(
                    'acceptedPayments', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                paymenttype = myconst.get('offers', )[0].get('policies', ).get('paymentType', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                checkinout = myconst.get('offers', )[0].get('policies', ).get('checkInOut', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                cancellation = myconst.get('offers', )[0].get('policies', ).get('cancellation', ),

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            mycontext = {
                'offerid': offerid,

                'citycode': citycode,
                'countrycode': countrycode,
                'availability': availability,
                'roomtype': roomtype,
                'roomcat': roomcat,
                'bed': bed,
                'bedtype': bedtype,
                'checkindate': checkindate,
                'checkout': checkout,
                'boardtype': boardtype,
                'typeestimated': typeestimated,
                'description': description,
                'guests': guests,
                'currency': currency,
                'base': base,
                'total': total,
                'pricevariations': pricevariations,
                'creitcards': creitcards,
                'acceptedPaymnts': acceptedPaymnts,
                'paymenttype': paymenttype,
                'checkinout': checkinout,
                'cancellation': cancellation,
                'hotelname': hotelname,

            }

            room = k
            context = {
                'mycontext': mycontext,
                'hoteldetailslist': hoteldetailslist,
                'hoteldetails': hoteldetails,
                'latitude': latitude,
                'longitude': longitude,
                'cityname': cityname,
                'line': line,
                'room': room,

            }

        print("---------------------------------------------------------------", offerid)

        return render(request, 'roomdetails.html', context)

    else:
        return render(request, 'roomdetails.html')


roomdetailslist = []


def bookingform(request, offerid):
    if request.method == 'POST':
        roomdetailslist.clear()
        hoteldetails = request.POST.get('hoteldetails', )
        roomdetails = request.POST.get('room', )
        roomdetails = eval(roomdetails)
        myconst = roomdetails

        checkindate = "Not availlable"
        checkout = "Not availlable"
        pricevariations = "Not availlable"
        creitcards = "Not availlable"
        acceptedPaymnts = "Not availlable"
        acceptedPayments = "Not availlable"

        paymenttype = "Not availlable"
        checkintime = "Not availlable"
        checkouttime = "Not availlable"
        cancellation = "Not availlable"
        total = "Not availlable"

        # percentage=
        base = "Not availlable"
        taxes = "Not availlable"
        currency = "Not availlable"

        try:
            checkindate = myconst.get('offers', )[0].get('checkInDate', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            checkout = myconst.get('offers', )[0].get('checkOutDate', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            pricevariations = myconst.get('offers', )[0].get('price', ).get('variations', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            creitcards = myconst.get('offers', )[0].get('policies', ).get('guarantee', ).get('acceptedPayments', ).get(
                'creditCards', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            acceptedPayments = myconst.get('offers', )[0].get('policies', ).get('guarantee', ).get(
                'acceptedPayments', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
            try:
                acceptedPayments = myconst.get('offers', )[0].get('policies', ).get('deposit', ).get(
                    'acceptedPayments', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

        try:
            paymenttype = myconst.get('offers', )[0].get('policies', ).get('paymentType', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            checkintime = myconst.get('offers', )[0].get('policies', ).get('checkInOut', ).get('checkIn', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            checkouttime = myconst.get('offers', )[0].get('policies', ).get('checkInOut', ).get('checkOut', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            cancellation = myconst.get('offers', )[0].get('policies', ).get('cancellation', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            total = myconst.get('offers', )[0].get('price', ).get('total', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            base = myconst.get('offers', )[0].get('price', ).get('base', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            taxes = myconst.get('offers', )[0].get('price', ).get('total', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        try:
            currency = myconst.get('offers', )[0].get('price', ).get('currency', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        if base == None:
            try:
                base = myconst.get('offers')[0].get('price').get('variations').get('changes')[0].get('base')
            except (KeyError, AttributeError, TypeError) as e:
                print(e)

        tax = "Not Avaiabe"
        try:
            tax = float(total) - float(base)
        except TypeError as e:
            print(e)
        print(tax)

        room = {

            'checkindate': checkindate,
            'checkout': checkout,
            'pricevariations': pricevariations,
            'creitcards': creitcards,
            'acceptedPayments': acceptedPayments,
            'paymenttype': paymenttype,
            'checkintime': checkintime,
            'checkouttime': checkouttime,
            'cancellation': cancellation,
            'total': total,

            # 'percentage':percentage ,
            'base': base,
            'tax': tax,
            'currency': currency,

        }
        roomdetailslist.append(room)

        k = eval(hoteldetails)

        media = "Not availlable"
        cityname = "Not availlable"
        hotelname = "Not availlable"
        line = "Not availlable"
        ammenitiesraw = "Not availlable"

        try:
            media = k.get('hotel', ).get('media', )[0].get('uri', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            cityname = k.get('hotel', ).get('address', ).get('cityName', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            hotelname = k.get('hotel', ).get('name', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            line = k.get('hotel', ).get('address', ).get('lines', )[0]

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            ammenitiesraw = k.get('hotel', ).get('amenities', )[:3]
        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        ammenities = []
        for i in ammenitiesraw:
            i = i.replace('_', ' ')

            i = i.lower()
            ammenities.append(i)

        context = {
            'offerid': offerid,
            'cityname': cityname,
            'hotelname': hotelname,
            'line': line,
            'media': media,
            'ammenities': ammenities,
            'roomdetailslist': roomdetailslist,
            'hoteldetails': hoteldetails,
        }

        print("---------------------------------------------------------------", offerid)

        return render(request, 'book.html', context)
    else:

        return render(request, 'book.html')


bookcontext = []


def book(request, offerid):
    bookcontext.clear()
    if request.method == 'POST':
        hoteldetails = request.POST.get('hoteldetails', )
        roomdetails = request.POST.get('roomdetails', )

        title = request.POST.get('title', )
        firstname = request.POST.get('FirstName', )
        lastname = request.POST.get('LastName', )
        phoneno = request.POST.get('phone', )
        email = request.POST.get('email', )
        cardVendorCode = request.POST.get('card_vendor_code', )
        Card_number = request.POST.get('card_number', )
        Expiry = request.POST.get('expiry', )
        # print(offerid, title, firstname, lastname, email, phoneno,cardVendorCode,Card_number,Expiry)
        offer = offerid

        k = eval(hoteldetails)
        room = eval(roomdetails)
        # print("this is expiry---------------------- ", Expiry)

        ammenitiesraw = "Not availlable"
        media = "Not availlable"
        cityname = "Not availlable"
        hotelname = "Not availlable"
        line = "Not availlable"
        latitude = "Not availlable"
        longitude = "Not availlable"
        phone = "Not availlable"

        try:
            ammenitiesraw = k.get('hotel', ).get('amenities', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            media = k.get('hotel', ).get('media', )[0].get('uri', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            cityname = k.get('hotel', ).get('address', ).get('cityName', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            hotelname = k.get('hotel', ).get('name', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            line = k.get('hotel', ).get('address', ).get('lines', )[0]

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        try:
            latitude = k.get('hotel', ).get('latitude', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            longitude = k.get('hotel', ).get('longitude', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)
        try:
            phone = k.get('hotel', ).get('contact', ).get('phone', )

        except (KeyError, AttributeError, TypeError) as e:
            print(e)

        # amadeus = Client(
        #     client_id='3MCFjLGhW3lJwBJtdAMirNGkc8FUoL4s',
        #     client_secret='OJEffyNYNtbPandi',
        #
        # )

        try:

            # offer = "OXZEHRM5GS"
            # #
            # guests = [{'id': 1, 'name': {'title': 'MR', 'firstName': 'BOB', 'lastName': 'SMITH'},
            #            'contact': {'phone': '+33679278416', 'email': 'bob.smith@email.com'}}]
            # payments = {'id': 1, 'method': 'creditCard',
            #             'card': {'vendorCode': 'VI', 'cardNumber': '4151289722471370', 'expiryDate': '2021-08'}}
            guests = [{'id': 1,'name': {'title': title, 'firstName': firstname, 'lastName': lastname},
                       'contact': {'phone': phone, 'email': email}}]
            payments = {'method': 'creditCard',
                        'card': {'vendorCode': cardVendorCode, 'cardNumber': Card_number,
                                 'expiryDate': Expiry}}  # '2021-08'

            hotel_booking = amadeus.booking.hotel_bookings.post(offer, guests, payments)

            data = hotel_booking.data
            # print('this is data',data)

        except ResponseError as error:
            print('this is ', error)
            return render(request, 'bookfailed.html', )



        else:
            confirmationID = "Not available"
            providerConfirmationId = "Not available"
            try:
                confirmationID = data[0].get('id', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                providerConfirmationId = data[0].get('providerConfirmationId', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            # try:
            #     offer_availability = amadeus.shopping.hotel_offer(offerid).get()
            #     # print('this is offer availlability', offer_availability.data)
            #     k = offer_availability.data
            #     # print('i have offer availlability')
            #
            # except ResponseError as error:
            #     print('this is ', error)
            #
            #
            # else:
            myconst = room

            checkindate = "Not availlable"
            checkout = "Not availlable"
            pricevariations = "Not availlable"
            creitcards = "Not availlable"
            acceptedPaymnts = "Not availlable"
            acceptedPayments = "Not availlable"

            paymenttype = "Not availlable"
            checkintime = "Not availlable"
            checkouttime = "Not availlable"
            cancellation = "Not availlable"
            total = "Not availlable"

            # percentage=
            base = "Not availlable"
            taxes = "Not availlable"
            currency = "Not availlable"

            try:
                checkindate = myconst.get('checkindate', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                checkout = myconst.get('checkout', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                pricevariations = myconst.get('pricevariations', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            # try:
            #     creitcards = myconst.get('offers', )[0].get('policies', ).get('guarantee', ).get(
            #         'acceptedPayments', ).get('creditCards', )
            #
            # except ( KeyError,AttributeError, TypeError ) as e:
            #     print(e)
            try:
                acceptedPayments = myconst.get('acceptedPayments')

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            # try:
            #     paymenttype = myconst.get('offers', )[0].get('policies', ).get('paymentType', )
            #
            # except ( KeyError,AttributeError, TypeError ) as e:
            #     print(e)
            try:
                checkintime = myconst.get('offers', )[0].get('policies', ).get('checkInOut', ).get('checkIn',
                                                                                                   )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                checkouttime = myconst.get('offers', )[0].get('policies', ).get('checkInOut', ).get(
                    'checkOut', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                cancellation = myconst.get('cancellation')

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                total = myconst.get('total', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                base = myconst.get('base', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)
            try:
                taxes = myconst.get('tax', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            try:
                currency = myconst.get('currency', )
            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            tax = "None"
            try:
                tax = float(total) - float(base)
            except (ValueError) as e:
                print(e)

            guests = " "

            try:
                guests = myconst.get('offers', )[0].get('guests', ).get('adults', )

            except (KeyError, AttributeError, TypeError) as e:
                print(e)

            booking = Bookings(first_name=firstname, last_name=lastname, email=email, phone=phoneno,

                               image=media, offerid=offerid, confirmationID=confirmationID,
                               providerConfirmationId=providerConfirmationId, Check_in=checkindate, Check_out=checkout,
                               Guests=guests, Price=total, currency=currency, hotel_name=hotelname, )
            booking.save()

            # sending booking mail
            ms = '''



                  <h1> Booking successfull.</h1>
                  <h3>Hello {firstname},</h3>
                  <br>Your booking Confirmation Id is : {confirmationID}.</br>
                  your provider confirmation ID is: { providerConfirmationId }




                  '''

            message = Mail(
                from_email='info@sky-swift.com',
                to_emails=email,
                subject='Hotel Booking',
                html_content=ms,

            )

            try:
                sg = SendGridAPIClient('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')
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)

            except Exception as e:
                print('not working', e)

            context = {
                'email': email,
                'firstname': firstname,

                'lastname': lastname,
                'phone': phone,
                'cityname': cityname,
                'latitude': latitude,
                'longitude': longitude,
                'line': line,
                'hotelname': hotelname,
                'checkindate': checkindate,
                'checkout': checkout,
                'pricevariations': pricevariations,
                'creitcards': creitcards,
                'acceptedPayments': acceptedPayments,
                'paymenttype': paymenttype,
                'checkintime': checkintime,
                'checkouttime': checkouttime,
                'cancellation': cancellation,
                'total': total,
                'confirmationID': confirmationID,

                'providerConfirmationId': providerConfirmationId,

                # 'percentage':percentage ,
                'base': base,
                'tax': tax,
                'currency': currency,
            }

            bookcontext.append(context)

    context = {
        'bookcontext': bookcontext,
    }
    return render(request, 'bookconf.html', context)

# #
# # def apicall(request):
# #     return render(request,'index.html')
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# from .utils import account_activation_token
#
#
# @sync_to_async
# def crunching_stuff():
#     sleep(20)
#     json_payload = {
#       "message": "Hello world"
#     }
#     print("Woke up after 10 seconds!")
#     return json_payload
#
# async def apicall(request):
#
#     """
#     or also
#     asyncio.ensure_future(crunching_stuff())
#     loop.create_task(crunching_stuff())
#     """
#
#     asyncio.create_task(crunching_stuff())
#     q=crunching_stuff()
#
#     context = {
#       'q':q
#     }
#     return render(request, 'index.html', context)
#
# #
# # def apicall(request):
# #   q=crunching_stuff()
# #   context={
# #     'q':q
# #   }
# #   return render(request, 'index.html',context)
#
#
# def loginfunction(request):
#     if request.method == 'POST':
#         pass
#     else:
#
#
#         return render(request,'login.html')
#
#
# def signup(request):
#     if request.method=='POST':
#         pass
#     else:
#         return render(request,'signup.html')
#
#
#
# def signup(request):
#     if request.method == "POST":
#         email = request.POST.get('email', False)
#         password = request.POST['password']
#         confirm_password = request.POST['confirmpassword']
#         print(email,password)
#
#         # if re.fullmatch(r'[A-Za-z0-9]{8,}', password):
#
#         if password == confirm_password:
#             # l, u, p, d = 0, 0, 0, 0
#             #
#             # s = password
#             # if (len(s) >= 8):
#             #     for i in s:
#             #
#             #         # counting lowercase alphabets
#             #         if (i.islower()):
#             #             l += 1
#             #
#             #         # counting uppercase alphabets
#             #         if (i.isupper()):
#             #             u += 1
#             #
#             #         # counting digits
#             #         if (i.isdigit()):
#             #             d += 1
#             #
#             #         # counting the mentioned special characters
#             #         if (i == '@' or i == '$' or i == '_'):
#             #             p += 1
#             # if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
#             #     print("Valid Password")
#             if User.objects.filter(email=email).exists():
#
#                 messages.warning(request, 'Email exists!')
#                 return render(request, 'signup.html')
#
#
#             else:
#                 user = User.objects.create_user(email=email, username=email, password=password
#                                                 )
#                 user.save()
#                 messages.success(request, 'Account created sucessfully!')
#                 user = authenticate(username=email, password=password)
#                 login(request,user)
#                 user.refresh_from_db()
#
#
#
#
#
#
#                 return redirect('/')
#
#             # else:
#             #     print("Invalid Password")
#             #     messages.warning(request, 'Password Must contain numbers,letters and Symbols!')
#             #
#             #     return render(request,'signup.html')
#
#         #         # send_mail(
#         #         #     'Account creation',
#         #         #     'Hello,welcome to the Maskani family. Your account creation was successful.Should you have any queries just send us an email or call our customer care numbers. here is a guide to get you started',
#         #         #     'firstregapp@gmail.com',
#         #         #     [email],
#         #         #     fail_silently=True,
#         #         #
#         #         # )
#         #
#         #         print("sign up sucessful")
#         #
#         #         return redirect('/')
#         # # else:
#         # return HttpResponse('invalid email')
#         else:
#             messages.info(request, 'Passwords do not match!')
#             return render(request,'signup.html')
#
#         # else:
#         #     return HttpResponse('password must contain charachters,numbers and uppercase letters')
#
#     else:
#         return render(request,'signup.html')
#
#
# def login_function(request):
#     if request.method=="POST":
#         username = request.POST.get('email', False)
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#
#
#
#
#                 return redirect('/')
#                 # return HttpResponse(f'{ profile }')#f'profileupdate/{pk}/update
#             else:
#                 messages.info(request, 'Your Account is Inactive')
#                 return render(request,'login.html')
#
#         else:
#             messages.info(request, 'Wrong username/Password!')
#             return render(request,'login.html')
#
#     else:
#         return render(request,'login.html')
#
#


#
#
#
