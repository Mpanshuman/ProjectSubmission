from django.db import models
from django import forms

# Create your models here.

class UserRegistrationdb(models.Model):
    userid = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length= 20)
    mobile = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.userid
    