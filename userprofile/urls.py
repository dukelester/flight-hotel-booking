from django.contrib import admin
from django.urls import path


from django.views.decorators.csrf import csrf_exempt

from .views import profilepage,Createprofile,UpdateProfile
urlpatterns = [

    path('<int:pk>/profileview', UpdateProfile.as_view(), name='profileview'),
    path('<int:pk>/update', UpdateProfile.as_view(), name='profileupdate'),

    ]