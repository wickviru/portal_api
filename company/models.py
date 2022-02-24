from django.db import models

class Auth(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=400)
    isAuth=models.BooleanField(default=False)
    isVerified=models.BooleanField(default=False)

class PersonalData(models.Model):
    userid=models.ForeignKey(Auth, on_delete=models.CASCADE)
    address = models.CharField(max_length=200,blank=True)
    area =  models.CharField(max_length=200,blank=True)
    phone = models.CharField(max_length=12,blank=True)
    link = models.CharField(max_length=300,blank=True)
    avatar =  models.CharField(max_length=300,blank=True)

