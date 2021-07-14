import json

import requests
from amadeus import Client, ResponseError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .models import EmailSubscribers
from django.shortcuts import get_object_or_404

from .models import EmailSubscribers


# Create your views here.


def hotels(request):
    try:
        user = User.objects.filter(username=request.user).get()
        context = {

            'user': user,

        }

        return render(request, 'postdetail.html', context)
    except User.DoesNotExist:

        context = {

        }

        return render(request, 'postdetail.html', context)


contextlist = []
inspirationList = []


def index(request):
    contextlist.clear()
    inspirationList.clear()
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()

        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip

    ip = get_ip(request)
    # print(ip)

    ip = ip

    url = f"http://ip-api.com/json/{ip}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    # print(response.text)
    k = response
    print(response)

    latitude = '1.2921'#k[]#"lat"
    longitude = '36.8219' # k[]#"lon"
    # print(country,countryCode,regionName,city,latitude, longitude)



    amadeus = Client(
        client_id='itAu7wJi164TVE1xgGnQ1hDTnnL7jchA',
        client_secret='3LlE97fVMg7AaWqG',
        hostname='test'
    )

    try:
        '''
        Returns activities for a location in Barcelona based on geolocation coordinates
        '''
        response = amadeus.shopping.activities.get(latitude=latitude, longitude=longitude)

        # print(response.data)
        k = response.data

        ep = k

        for ids in ep:
            myid = ids['id']

            try:
                '''
                Returns information of an activity from a given Id
                '''
                response = amadeus.shopping.activity(myid).get()
                # print(response.data)
                k = response.data

                ep = k

                name = ep['name']
                shortdes = ep['shortDescription']

                geocode = ep['geoCode']
                lattitude = geocode['latitude']
                longitude = geocode['longitude']
                rating = ep['rating']
                pictures = ep['pictures'][0:40]
                bookinglink = ep['bookingLink']
                currency = ep['price']['currencyCode']
                ammount = ep['price']['amount']

                mydict = {

                    'name': name,
                    'lattitude': lattitude,
                    'longitude': longitude,
                    'rating': rating,
                    'pictures': pictures,
                    'bookinglink': bookinglink,
                    'ammount': ammount,
                    'currency': currency,

                }

                contextlist.append(mydict)


            except ResponseError as error:
                raise error

    except ResponseError as error:
        raise error



    try:
        user = User.objects.filter(username=request.user).get()
        context = {

            'user': user,
            'contextlist': contextlist,
          
          
        }

        return render(request, 'homepage.html', context)
    except User.DoesNotExist:

        context = {

            'contextlist': contextlist,
           
           
        }

        return render(request, 'homepage.html', context)


def callcenter_view(request):
    return render(request, 'call.html')


def jobsview(request):
    return render(request, 'jobs.html')


def jobview(request):
    return render(request, 'job.html')


@login_required
def bookingconfirmview(request):
    return render(request, 'bookconf.html')




@login_required()
def profilepage(request):
    return render(request, 'profile.html')


#
#
# def homepagecontent(request):
#     from amadeus import Client, ResponseError
#
#     amadeus = Client(
#         client_id='nMwjEiAF4ocrNtIfjeh97aoO4yAyWw1A',
#         client_secret='zdmVihNx6DoB8KB0',
#         hostname='production'
#     )
#
#     try:
#         '''
#         What are the popular places in Barcelona (based on a geo location and a radius)
#         '''
#         response = amadeus.reference_data.locations.points_of_interest.get(latitude=41.397158, longitude=2.160873)
#
#         k = response.data
#
#         context = {
#             'k': k
#         }
#
#         return render(request, 'homepagecontent.html', context)
#
#     except ResponseError as error:
#         raise error
#

def mailsubscription(request):
    if request.method == "POST":
        email = request.POST['email']


        subscriber = EmailSubscribers(email=email)

        subscriber.save()


        message = Mail(
            from_email='campaigns@sky-swift.com',
            to_emails=email,
            subject='Newsletter subscription',
            html_content='<strong>Thank you for subscribing!</strong>')
        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)

        except Exception as e:
            print('not working')

    return render(request,'subscription_successfull.html')


def sendmarketingmails(request):
    emailu_subscribers = EmailSubscribers.objects.all()

    for email_subscriber in emailu_subscribers:
        email = email_subscriber.email
        message = Mail(
            from_email='campaigns@sky-swift.com',
            to_emails=email,
            subject='Newsletter subscription',
            # html_content=Marketting_emails.objects.filter(time_created=)

        )
        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)

        except Exception as e:
            print('not working')


#
# lists=EmailSubscribers.objects.all()
# print(lists)


def Cryptoform(request):
    return render(request, 'crypto form.html')


def Crypto(request):
    if request.method == 'POST':
        ammount = request.POST['ammount']
        currency = request.POST['currency']
        cryptocurrency = request.POST['paycurrency']

        values = {

            'price_amount': ammount,
            'price_currency': currency,
            'pay_currency': cryptocurrency,

        }
        payload = json.dumps(values)

        url = "https://api.sandbox.nowpayments.io/v1/payment"

        # payload = "{\n  \"price_amount\": 3999.5,\n  \"price_currency\": \"usd\",\n  \"pay_amount\": 0.8102725,\n  \"pay_currency\": \"btc\",\n  \"ipn_callback_url\": \"https://nowpayments.io\",\n  \"order_id\": \"RGDBP-21314\",\n  \"order_description\": \"Apple Macbook Pro 2019 x 1\",\n  \"case\" : \"success\"\n}"
        headers = {
            'x-api-key': 'M12PEZP-SN6MSAK-KAC0WDZ-SHRJNW1',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()

        paymentid = response['payment_id']
        print(paymentid)

        # print(response.text)

        url = f"https://api.sandbox.nowpayments.io/v1/payment/{paymentid}"
        payload = {}
        headers = {
            'x-api-key': 'M12PEZP-SN6MSAK-KAC0WDZ-SHRJNW1',
            'ipn_callback_url': 'KqwXVXnOA3WRuEk8nQ+5rg06RVotW5Cl'

        }

        response = requests.request("GET", url, headers=headers, data=payload).json()

        print(response)

        status = response['payment_status']

        while True:

            url = f"https://api.sandbox.nowpayments.io/v1/payment/{paymentid}"
            payload = {}
            headers = {
                'x-api-key': 'M12PEZP-SN6MSAK-KAC0WDZ-SHRJNW1',
                'ipn_callback_url': 'KqwXVXnOA3WRuEk8nQ+5rg06RVotW5Cl'

            }

            response = requests.request("GET", url, headers=headers, data=payload).json()

            print(response)

            status = response['payment_status']
            if status == 'finished':
                print('sucessful')
                break

            elif status == 'failed':
                print('failed')
                break


            else:
                print(status)

    return redirect('/')


def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "500.html", context=context)
    response.status_code = 500
    return response


def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response



def verify(request):
    return render(request,'verifyforzoho.hrml')




def terms(request):
    return render(request,'Terms.html')

def acceptable_use_policy(request):
    return render(request,'Acceptable_info_tech_policy.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')


def carreers(request):
    return render(request, 'careers.html')



def unsubscribe(request):

    if request.method=="POST":
        email=request.POST['email']
        subscriber= get_object_or_404(EmailSubscribers, email=email)
        try:

            subscriber.delete()
        except:
            raise Http404("Subscriber does not exist")
        return render(request, 'unsubscribe.html')

    else:
        return render(request, 'unsubscribeform.html')



