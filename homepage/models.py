from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
import os
import datetime
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received



def show_me_the_money(sender, **kwargs):
    print("MAY be")

def orphanage_image_upload_url(instance, filename):
    return os.path.join("orphanage_image", str(instance.orphanage_name), filename)

def company_image_upload_url(instance, filename):
    return os.path.join("company_image", str(instance.company_name), filename)


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
    phone_no = models.CharField(max_length=10,null=True)

class Orphanage(models.Model):
    orphanage_id = models.OneToOneField(User, on_delete=models.CASCADE)
    orphanage_name = models.CharField(max_length=30)
    year_of_establishment = models.IntegerField()
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10,null=True)
    image = models.ImageField(upload_to=orphanage_image_upload_url, blank=True, null=True)
    description = models.CharField(max_length=300)
    account = models.CharField(max_length=300,default = None , null=True)
    status=models.CharField(max_length=50,default='Freshly Applied')


class CateringCompany(models.Model):
    company_id=models.ForeignKey(User,on_delete=models.PROTECT,default=None)
    company_name = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to=company_image_upload_url, blank=True, null=True)


class review(models.Model):
    company=models.ForeignKey(CateringCompany,on_delete=models.PROTECT,default=None)
    description=models.CharField(max_length=150,null=True)
    rating=models.IntegerField(null=True)
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    date_created=models.DateField(default=None)



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
    orphanage_name = models.CharField(default=None,max_length=100)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.PROTECT)
    status = models.IntegerField()
    date_of_donation = models.DateTimeField(default = timezone.now)
    description = models.CharField(default=None,max_length=50)
    paypal_transaction = models.CharField(default=None,max_length=50)

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
    donation_type = models.CharField(max_length=1,choices=TYPE)
    orphanage_name = models.CharField(default=None,max_length=100)
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
    canbereviewed=models.CharField(max_length=30,default='No')

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
    companyname=models.ForeignKey(CateringCompany,on_delete=models.PROTECT)
    user_id=models.ForeignKey(User,on_delete=models.PROTECT,default=None)
    token=models.CharField(max_length=40)
    hit = models.DateTimeField(default=datetime.datetime.now())


valid_ipn_received.connect(show_me_the_money)



class catering(models.Model):
    event_id=models.IntegerField()
    company_name=models.CharField(max_length=50)
    items=models.CharField(max_length=500,default=None)
    price=models.CharField(max_length=500,default=None)
    status=models.CharField(max_length=20,default='Not Accepted')
    image=models.CharField(max_length=100,null=True)