from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Service_Photo(models.Model):
    phote_name = models.CharField(max_length=255, null=True)
    zabzor_images = models.ImageField(null=True, blank=True, upload_to='media')
        
    def __str__(self):
        return "{}".format (self.phote_name)


class Customer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200, null=True)
    customer_phoneNumber = models.CharField(max_length=10, null=True)
    service_photo = models.ForeignKey(Service_Photo, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.customer_name) 
