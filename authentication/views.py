# Create your views here.

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from userprofile.models import Profile

from .utils import account_activation_token


def loginpage(request):
    return render(request, 'login.html')


def signuppage(request):
    return render(request, 'register.html')


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email', False)
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        # if re.fullmatch(r'[A-Za-z0-9]{8,}', password):

        if password == confirm_password:

            if User.objects.filter(email=email).exists():

                messages.warning(request, 'Email exists!')
                return render(request, 'register.html')


            else:
                user = User.objects.create_user(email=email, username=email, password=password
                                                )
                user.is_active = False
                user.save()
                messages.success(request, 'Account created sucessfully!')
                user.refresh_from_db()

                uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                token=account_activation_token.make_token(user)
                domain = get_current_site(request)
                domain=domain.domain
                link=reverse('activate',kwargs={'uidb64':uidb64,'token':token})
                print(token)
                activation_url=f'http://{domain}{link}'


                ms = render_to_string('emailconfirmation.html', {'url': activation_url,'email':email})
                message = Mail(
                                        from_email='accounts@sky-swift.com',
                                        to_emails=email,
                                        subject='Account Creation',
                                        html_content=ms,

                                    )

                try:
                    #sg = SendGridAPIClient('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')
                    sg=SendGridAPIClient('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')
                    response = sg.send(message)
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)

                except Exception as e:
                    print('not working', e)

                print("sign up sucessful")
                messages.info(request, 'Please check your email to confirm registration')


                return render(request,'register.html')


        else:
            messages.info(request, 'Passwords do not match!')
            return render(request,'register.html')

        # else:
        #     return HttpResponse('password must contain charachters,numbers and uppercase letters')

    else:
        return render(request,'register.html')


def login_function(request):
    if request.method=='POST':
        username = request.POST.get('email', False)
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                profile = Profile.objects.filter(user=request.user).get()
                pk = profile.pk


                return redirect(f'{pk}/update')
                # return HttpResponse(f'{ profile }')#f'profileupdate/{pk}/update
            else:
                messages.info(request, 'Your Account is Inactive')
                return render(request,'login.html')

        else:
            messages.info(request, 'Wrong username/Password!')
            return render(request,'login.html')

    else:

        return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('/loginpage/')




def google_login(request):
    redirect_url = "%s://%s%s" % (
        request.scheme, request.get_host(), reverse('google_login')
    )
    if ('code' in request.GET):
        params = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'redirect_uri': redirect_url,
            'client_id': settings.GP_CLIENT_ID,
            'client_secret': settings.GP_CLIENT_SECRET
        }
        url = 'https://accounts.google.com/o/oauth2/token'
        response = requests.post(url, data=params)
        url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        access_token = response.json().get('access_token')
        response = requests.get(url, params={'access_token': access_token})
        user_data = response.json()
        email = user_data.get('email')

        if email:
            user, _ = User.objects.get_or_create(email=email, username=email)
            gender = user_data.get('gender', '').lower()
            if gender == 'male':
                gender = 'M'
            elif gender == 'female':
                gender = 'F'
            else:
                gender = 'O'
            data = {
                'first_name': user_data.get('name', '').split()[0],
                'last_name': user_data.get('family_name'),
                'google_avatar': user_data.get('picture'),
                'gender': gender,
                'is_active': True
            }
            user.__dict__.update(data)
            user.save()
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)
        else:
            messages.error(
                request,
                'Unable to login with Gmail Please try again'
            )
        return redirect('/')
    else:
        url = "https://accounts.google.com/o/oauth2/auth?client_id=%s&response_type=code&scope=%s&redirect_uri=%s&state=google"
        scope = [
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email"
        ]
        scope = " ".join(scope)
        url = url % (settings.GP_CLIENT_ID, scope, redirect_url)
        return redirect(url)


discoverHomesList = []








from django.views.generic import View


class Verification(View):
    def get(self,request,uidb64,token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            print(id)
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message=' + 'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            profile = Profile.objects.filter(user=request.user).get()
            pk = profile.pk
            return redirect(f'{pk}/update')

        except Exception as ex:
            print(ex)
            pass
        return redirect('/')