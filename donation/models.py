from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


# Create your models here.

class donatemoney(models.Model):
    tid = models.AutoField(primary_key=True)                       
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    transfer = models.CharField(max_length=264,default=0)
    amount = models.IntegerField(default=0)
    orphanage = models.CharField(max_length=264)
 #   date_of_donation = models.DateTimeField(default = timezone.now)
    description = models.CharField(default=None,max_length=50)

class donatevaluables(models.Model):
    TYPE = (
        ('F','Food'),
        ('C','Clothes'),
        ('B','Book'),
        ('E','Eletrical Appliances'),
        ('O','other'),
    )
    tid = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=15)
    donation_type = models.CharField(max_length=1,choices=TYPE)
 #   date_of_donation = models.DateTimeField(default = timezone.now)
    weight = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    breadth = models.IntegerField()
    description = models.CharField(default=None,max_length=100)
    status = models.IntegerField()

    
    
    

