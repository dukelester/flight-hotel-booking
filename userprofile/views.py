from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from hotels.models import Bookings
from userprofile.models import Profile


@login_required()
def profilepage(request):
    profile=Profile.objects.filter(user=request.user).get()
    bookings=Bookings.objects.all()


    context={
        'profile':profile,
        'bookings':bookings,
    }

    return render(request, 'profile.html', context)



class Createprofile(LoginRequiredMixin,CreateView):
    template_name = 'profile.html'
    model = Profile
    fields = [ 'first_name' ,"last_name", " postal_address", "physical_adress" , "profile_picture", "email" ,"phone_number"]
    success_url = '/'




class UpdateProfile(LoginRequiredMixin,UpdateView):
    template_name = 'profile.html'
    model = Profile
    fields = [ 'first_name' ,"last_name",'physical_adress','postal_address', "physical_adress" , "profile_picture", "email" ,"phone_number"]
    success_url = 'profileview'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        bookings = Bookings.objects.filter(user=self.request.user)
        context['bookings'] = bookings

        return context






