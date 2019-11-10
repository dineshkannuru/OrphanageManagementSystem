from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os


# Create your models here.

def image_upload_url(instance, filename):
    return os.path.join("orphanage_image", str(instance.id), filename)


class Type(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_no = models.IntegerField()


class UserDetails(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    phone_no = models.IntegerField()


class Orphanage(models.Model):
    orphanage_id = models.ForeignKey(User, on_delete=models.CASCADE)
    orphanage_name = models.CharField(max_length=30)
    year_of_establishment = models.IntegerField()
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    address = models.CharField(max_length=50)
    phone_no = models.IntegerField(null=True)
    image = models.ImageField(upload_to=image_upload_url, blank=True, null=True)
    description = models.CharField(max_length=300)
    account = models.CharField(max_length=300)


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


class MoneyDonation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.PROTECT)
    date_of_donation = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=50)
    amount = models.IntegerField()


class Donation(models.Model):
    TYPE = (
        ('F', 'Food'),
        ('C', 'Clothes'),
        ('B', 'Book'),
        ('E', 'Eletrical Appliances'),
        ('O', 'other'),
    )
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.CASCADE)
    date_of_donation = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()
    donation_type = models.CharField(max_length=1, choices=TYPE)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()


class Emergency(models.Model):
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=100)
    situation = models.CharField(max_length=500)
    date_of_post = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()


class Transport(models.Model):
    danation_id = models.ForeignKey(Donation, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    cost = models.IntegerField()

class donatemoney(models.Model):
    tid = models.AutoField(primary_key=True) 
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    transfer = models.CharField(max_length=264,default=0)
    amount = models.IntegerField(default=0)
    orphanage_id = models.ForeignKey(Orphanage, on_delete=models.PROTECT)
    status = models.IntegerField()
 #   date_of_donation = models.DateTimeField(default = timezone.now)
    description = models.CharField(default=None,max_length=50)
    
    class Meta:
        get_latest_by = ['tid']

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
    date_of_donation = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()
    description = models.CharField(default=None,max_length=100)
    status = models.IntegerField()

    class Meta:
        get_latest_by = ['tid']