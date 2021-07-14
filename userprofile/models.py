from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    postal_address= models.CharField(max_length=200, blank=True)
    physical_adress= models.CharField(max_length=300, blank=True)
    profile_picture = models.ImageField(upload_to='media', null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    payment_methods=models.CharField(max_length=255,default=0)
    physical_address=models.CharField(max_length=255,default=0)





