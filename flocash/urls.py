from django.urls import path

from . import views

urlpatterns = [
    path('flocash', views.flocashView, name='flocashPayment'),
    path('webhook', views.webhook, name='webhook'),
]
