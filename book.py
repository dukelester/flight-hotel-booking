


from amadeus import Client, ResponseError
import time
amadeus = Client(
            client_id='3MCFjLGhW3lJwBJtdAMirNGkc8FUoL4s',
            client_secret='OJEffyNYNtbPandi',

        )

try:

    # hotels_by_city = amadeus.shopping.hotel_offers.get(cityCode='LON')
    # print(hotels_by_city.data)
    # Get list of offers for a specific hotel
    hotel_offers = amadeus.shopping.hotel_offers_by_hotel.get(hotelId = 'WHLON464')
    print(hotel_offers.data)
    # hotel_offers = amadeus.shopping.hotel_offers_by_hotel.get(hotelId=hotelid)
    # time.sleep(10)
    # offer="Q93XA8LC1W"
    #
    # guests = [{'id': 1, 'name': {'title': 'MR', 'firstName': 'BOB', 'lastName': 'SMITH'},
    #            'contact': {'phone': '+33679278416', 'email': 'bob.smith@email.com'}}]
    # payments = {'id': 1, 'method': 'creditCard',
    #             'card': {'vendorCode': 'VI', 'cardNumber': '4151289722471370', 'expiryDate': '2021-08'}}
    # # guests = [{'name': {'title': title, 'firstName': firstname, 'lastName': lastname},
    # #            'contact': {'phone': phone, 'email': email}}]
    # # payments = {'method': 'creditCard',
    # #             'card': {'vendorCode': cardVendorCode, 'cardNumber': Card_number,
    # #                      'expiryDate': Expiry}}  # '2021-08'
    # #
    # hotel_booking = amadeus.booking.hotel_bookings.post(offer, guests, payments)
    #
    # data = hotel_booking.data
    # print('this is data',data)

except ResponseError as error:
    raise error