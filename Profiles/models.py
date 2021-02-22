from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class createProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=250)
    date_of_birth=models.DateField()
    email_id=models.EmailField(max_length=120)
    phonenumber=models.IntegerField(unique=True)
    branch=models.CharField(max_length=120)

    def __str__(self):
        return self.phonenumber


    def get_absolute_url(self):
        return reverse('success', kwargs={'slug': self.slug})


class AccountInfoModel(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    accno=models.CharField(max_length=120,unique=True)
    balance=models.IntegerField()
    mpin=models.IntegerField(unique=True)
    ifs_code=models.CharField(max_length=12)

    def __str__(self):
        return self.balance

    # def get_absolute_url(self):
    #     return reverse('success', kwargs={'slug':self.slug})

class TransferModel(models.Model):
    mpin=models.CharField(max_length=4)
    accno=models.CharField(max_length=6)
    amount=models.IntegerField()

    def __str__(self):
        return  self.accno

    # def get_absolute_url(self):
    #     return reverse('success', kwargs={'slug':self.slug})