from django import forms
from django.db import models

# Create your forms here.

class donatemoneyform(forms.Form):
    tid = forms.IntegerField()
    user_name = forms.CharField()
    transfer = forms.CharField()
    amount = forms.IntegerField()
    date_of_donation = forms.DateTimeField()
    description = forms.CharField()
    orphanage = forms.CharField()

class donatevaluablesform(forms.Form):
    tid = forms.IntegerField()
    user_name = forms.CharField()
    uid = forms.IntegerField()
    type = forms.CharField()
    weight = forms.IntegerField()
    length = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()

