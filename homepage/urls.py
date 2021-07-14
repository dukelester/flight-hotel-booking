from django.urls import path, include

from .views import mailsubscription, Crypto, Cryptoform, jobsview, jobview

from .views import bookingconfirmview, terms, acceptable_use_policy
from .views import index, callcenter_view, privacy_policy, carreers, unsubscribe

from . import views

urlpatterns = [

    path('', index, name='index'),
    path('index', index, name='index'),
    path('terms', terms, name='terms'),
    path('use_policy', acceptable_use_policy, name='use_policy'),

    path('callcenter', callcenter_view, name='callcenter'),
    path('jobs.html', jobsview, name='jobs'),
    path('job.html', jobview, name='job'),
    path('bookconfirm', bookingconfirmview, name='bookconfirm'),

    path('privacypolicy', privacy_policy, name='privacypolicy'),
    path('careers', carreers, name='careers'),

    path('mailsubscription', mailsubscription, name='mailsubscription'),
    path('unsubscribe', unsubscribe, name='unsubscribe'),
    path('crypto', Cryptoform, name='cryptoform'),
    path('Crypto', Crypto, name='crypto'),

    # path('', include('flights.urls')),
    path('', include('hotels.urls')),
    path('', include('userprofile.urls')),
    path('', include('authentication.urls')),
    path('', include('book.urls')),
    path('', include('flocash.urls')),

]

handler404 = views.handler404
handler500 = views.handler500
