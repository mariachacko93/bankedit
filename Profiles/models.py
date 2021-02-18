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


    def __str__(self):
        return self.phonenumber


    def get_absolute_url(self):
        return reverse('success', kwargs={'slug': self.slug})