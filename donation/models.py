from django.db import models
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received

def show_me_the_money(sender, **kwargs):
    print("MAY be")

# Create your models here.
print("will it work")
valid_ipn_received.connect(show_me_the_money)

