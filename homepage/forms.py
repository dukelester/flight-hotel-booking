from django import forms
from  .models import Profile

class ProfilePage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'phone_number', 'email', 'bio', 'location','user']