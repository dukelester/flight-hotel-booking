# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Payments(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
