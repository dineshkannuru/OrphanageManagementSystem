from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
import os

def image_upload_url(instance, filename):
    return os.path.join("orphanage_image", str(instance.orphanage_name), filename)

class Type(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ref_no = models.IntegerField()

class UserDetails(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    phone_no = models.IntegerField()

class Orphanage(models.Model):
    orphanage_id = models.OneToOneField(User, on_delete=models.CASCADE)
    orphanage_name = models.CharField(max_length=30)
    year_of_establishment = models.IntegerField()
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    address = models.CharField(max_length=50)
    phone_no = models.IntegerField(null=True)
    image = models.ImageField(upload_to=image_upload_url, blank=True, null=True)
    description = models.CharField(max_length=300)
    account = models.CharField(max_length=300,default = None , null=True)
    status=models.CharField(max_length=50,default='Freshly Applied')

class Orphan(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.CASCADE)
    orphan_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    special_skills = models.CharField(max_length=50)

class AddOrphan(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    find_place = models.CharField(max_length=100)
    ref_no = models.IntegerField()
    date_of_birth = models.DateField()

class donatemoney(models.Model):
    tid = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    transfer = models.CharField(max_length=264,default=0)
    amount = models.IntegerField(default=0)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.PROTECT)
    status = models.IntegerField()
    date_of_donation = models.DateTimeField(default = timezone.now)
    description = models.CharField(default=None,max_length=50)
    
    class Meta:
        get_latest_by = ['tid','status']

class donatevaluables(models.Model):
    TYPE = (
        ('F','Food'),
        ('C','Clothes'),
        ('B','Book'),
        ('E','Eletrical Appliances'),
        ('O','other'),
    )
    tid = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.PROTECT)
    orphanage_name = models.CharField(default=None,max_length=100)
    donation_type = models.CharField(max_length=1,choices=TYPE)
    date_of_donation = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()
    object_name = models.CharField(default=None,max_length=100)
    address = models.CharField(default=None,max_length=100)
    description = models.CharField(default=None,max_length=100)
    status = models.IntegerField()

    class Meta:
        get_latest_by = ['tid','status']

class Emergency(models.Model):
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=100)
    situation = models.CharField(max_length=500)
    date_of_post = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()

class Events(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.PROTECT)
    date_of_event = models.DateField()
    date_of_post = models.DateField(default=date.today())
    status = models.CharField(max_length=50,default='Freshly Applied')
    description = models.CharField(max_length=200)
    event = models.CharField(max_length=30)

class Transport(models.Model):
    danation_id = models.IntegerField()
    company_name = models.CharField(max_length=50)
    cost = models.IntegerField()
    type=models.CharField(max_length=20)
    duration=models.CharField(max_length=20)
    status=models.CharField(max_length=30,default='Not Accepted')

class success(models.Model):
    orphanage_id = models.OneToOneField(Orphanage,on_delete=models.CASCADE)
    status= models.CharField(max_length=30,default='Freshly Applied')


class verification(models.Model):
    companyname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    token=models.CharField(max_length=40)
