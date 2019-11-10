import twitter
import facebook
from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from homepage.models import donatemoney,donatevaluables,Orphanage
from donation.forms import donatemoneyform,donatevaluablesform
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def donatemoneyview(request):
    Orphanages = Orphanage.objects.all()
    if request.method =='POST':
        user_id = request.user
        transfer = request.POST['transfer']
        amount = request.POST['amount']
        orphanage_id1 = request.POST['orphanage_id']
        orphanage = Orphanage.objects.get(pk = orphanage_id1)
        print(orphanage_id1)
        description= request.POST['description']
        status = "0"
        saveform = donatemoney.objects.create(user_id=user_id,transfer=transfer,amount=amount,orphanage_id=orphanage,description=description,status=status)
        saveform.save()
        tid=donatemoney.objects.latest('tid')
        tidstring=tid.tid
        if transfer=="paypal":
            return HttpResponseRedirect(reverse('donation:inprogress',args=(tidstring,amount,orphanage_id1)))
    else:
        context = {
            'orphanages': Orphanages
        }
    return render(request,'donation/money.html',context)

def donation_completedview(request):
    return render(request,'donation/donation_completed.html')


def donatevaluablesview(request):
    Orphanages = Orphanage.objects.all()
    Orphanages = Orphanage.objects.all()
    if request.method =='POST':
        user_id = request.user
        type=request.POST.get('type')
        quantity=request.POST.get('quantity')
        orphanage_id1 = request.POST['orphanage_id']
        orphanage = Orphanage.objects.get(pk = orphanage_id1)
        description= request.POST.get('description')
        print(quantity)
        status='0'
        saveform = donatevaluables.objects.create(user_id=user_id,donation_type=type,orphanage_id=orphanage,quantity=quantity,description=description,status=status)
        saveform.save()
        return HttpResponseRedirect(reverse('donation:completed'))
    else:
        context = {
            'orphanages': Orphanages
        }
        return render(request, 'donation/valuables.html',context)

def paypal_home(request,tid,amount,orphanage_id1): 
    selected_orphanage=Orphanage.objects.get(pk = orphanage_id1)
    orphanage=selected_orphanage.orphanage_name
    user_name=request.user.get_full_name()
    account=selected_orphanage.account
    print(account)
    paypal_dict = {
        "business": account,
        "amount": amount,
        "currency-code":"USD",
        "item_name": tid,
        "invoice": tid,
        "notify_url": "http://57e8e544.ngrok.io/donation/HaSHinGLinKK/",
        "return": "http://127.0.0.1:8000/paypal_return/",
        "cancel_return": "http://127.0.0.1:8000/paypal_cancel/",
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    data=donatemoney.objects.latest()
    context = {"form": form,"data":data,"user_name":user_name,"orphanage":orphanage}
    return render(request, "donation/gatewaypage.html", context)

def paypal_cancel(request):
     return render(request,'donation/paypalcancel.html')

@csrf_exempt
def paypal_return(request):
   
   #Code to change status to 1 for money 
    
   # consumer_key=''
   # consumer_secret=''
   # access_token=''
   # access_secret=''

   # api = twitter.Api(consumer_key=consumer_key,
   #                   consumer_secret=consumer_secret,
   #                   access_token_key=access_token,
   #                   access_token_secret=access_secret)
    
   # post_update = api.PostUpdates(status='My first tweet through django')
   return render(request,'donation/paypalreturn.html')

def facebookview(request):
    token='EAALOtHuxZAWUBAMZCC0uefyOq0ZCwN9CKi402YpNuc16UnjhCQovj8LXEuZCFCibPh6vPID7ZAhT4uXiRFsSWTnCycHVTMhgGfVlc1vGULC7ZA2ZB54rVPjZA1iMZAUNA7ZBpaNLWHveGHOu0t5HWE8GF4ssBfVyNl26MBHynbPFP6t0iXwnWk2ColCtlZCdzXAZCkAzKoROFOagtF5b8pIkT0Eb'
    fb = facebook.GraphAPI(access_token=token)
    #faceb = OpenFacebook(access_token=token)
    fb.put_object(parent_object='me',connection_name='feed',message='Test1')
    #faceb.set('me/feed', message='Test1',url='http://www.something')
   



