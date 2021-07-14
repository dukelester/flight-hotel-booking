from django.db import models

# Create your models here.

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Hotels(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    rooms_availlable = models.CharField(max_length=200)
    # destination= models.CharField(max_length=300)
    # departure_time = models.CharField(max_length=300)
    expected_arrival_time = models.CharField(max_length=300)
    price=models.IntegerField()
    location=models.CharField(max_length=200,blank=True)
    picture = CloudinaryField('image')
    date_posted=models.DateTimeField(auto_now_add=True)






    # def get_absolute_url(self):
    #     return reverse('flight', args=(str(self.id)))

    def __str__(self):
        return self.Airline





class Bookings(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=40)
    confirmationID=models.CharField(max_length=40)
    providerConfirmationId=models.CharField(max_length=40)
    Check_in=models.CharField(max_length=40)
    Check_out=models.CharField(max_length=40)
    Guests=models.CharField(max_length=40)
    Price=models.CharField(max_length=40)
    hotel_name=models.CharField(max_length=10)
    currency=models.CharField(max_length=10,null=True)
    image= models.ImageField(upload_to='media')
    offerid=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=300,null=True)
    class Meta:
        verbose_name_plural = "Bookings"