from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

from  django.utils import  timezone





class EmailSubscribers(models.Model):
    email=models.EmailField(max_length=54)

    class Meta:
        verbose_name_plural = "Email Subscribers"



class MarkettingEmail(models.Model):
    thistime = timezone.now()
    email=RichTextField()
    time_created=models.CharField(default=thistime,blank=False,max_length=256)
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Marketting Emails"

