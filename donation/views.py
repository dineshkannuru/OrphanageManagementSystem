import twitter
import facebook
import json
import requests
from json import load
from urllib.request import urlopen
from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from homepage.models import donatemoney,donatevaluables,Orphanage
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url='registration:login')
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

@login_required(login_url='registration:login')
def donatevaluablesview(request):
    Orphanages = Orphanage.objects.all()
    Orphanages = Orphanage.objects.all()
    if request.method =='POST':
        user_id = request.user
        type=request.POST.get('type')
        quantity=request.POST.get('quantity')
        orphanage_id1 = request.POST['orphanage_id']
        orphanage=Orphanage.objects.get(pk = orphanage_id1)
        orphanage_name = orphanage.orphanage_name
        object = request.POST.get('object_name')
        orphanage = Orphanage.objects.get(pk = orphanage_id1)
        description= request.POST.get('description')
        address = request.POST.get('address')
        print(user_id)
        status='0'
        saveform = donatevaluables.objects.create(user_id=user_id,donation_type=type,orphanage_name=orphanage_name,object_name=object,orphanage_id=orphanage,quantity=quantity,description=description,address=address,status=status)
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
    user_name=request.user
    account=selected_orphanage.account
    print(account)
    paypal_dict = {
        "business": account,
        "amount": amount,
        "currency-code":"USD",
        "item_name": tid,
        "invoice": tid,
        "notify_url": "http://57e8e544.ngrok.io/donation/HaSHinGLinKK/",
        "return": "http://127.0.0.1:8000/donation/money/",
        "cancel_return": "http://127.0.0.1:8000/donation/money/",
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    data=donatemoney.objects.latest()
    context = {"form": form,"data":data,"user_name":user_name,"orphanage":orphanage}
    return render(request, "donation/gatewaypage.html", context)

def paypal_cancel(request):
     return render(request,'donation/paypal_cancel.html')


#return url is mistake
@csrf_exempt
def paypal_return(request):
   data=donatemoney.objects.latest()
   data.status='1'
   data.save()
   return render(request,'donation/paypal_return.html')

def rejectedview(request):
    user = request.user
    rejected = donatevaluables.objects.filter(user_id=user,status=-2)
    
    context = {"rejected":rejected}
    return render(request, "donation/Rejected.html", context)


def acceptedview(request):
    user = request.user
    accepted = donatevaluables.objects.filter(user_id=user,status=-1)
    
    context = {"accepted": accepted}
    return render(request, "donation/Accepted.html", context)

def history(request):
    user = request.user
    donations = donatemoney.objects.filter(user_id=user)
    
    context = {"donations": donations}
    return render(request, "donation/Accepted.html", context)




#COULD not access 2d list in django
def socialview(request):
    url="https://graph.facebook.com/v5.0/107316914058945?fields=posts.limit(20)%7Bmessage%2Cfrom%2Cadmin_creator%2Clikes.limit(30)%2Cfull_picture%7D%2Cevents.limit(10)%7Bowner%2Cdescription%2Cstart_time%7D&access_token=EAALOtHuxZAWUBANT76cZC0rRVlFDrwXrReqBWC4jiotiZCZAI7KIp9Glc1yakdJ1rJG0V8mRxNYGiIaKlHbc3dIVXWzPUOImGjVp8kxAQb71p7d2t4Kk5W2LzIwEnrpfDUQbiN1vHH2gUJR9QLmP9hBnLOsKZBDjYWFq7Dn6cc3ZAMLSVaXBZBRYlzSIuO9G6ZB4kevqTwh0DgZDZD"
    response=urlopen(url)
    json_text = load(response)
    
    feed_messages=list()
    feed_pictures=list()
    event_owner=list()
    event_description=list()
    event_start=list()
    
    feed = [[] for i in range(10)]
   

    for info in json_text["posts"]["data"]:
        mess=info.get('message', 'null')
        pics=info.get('full_picture','null')
        likes=info.get('likes','null')
        feed_messages.append(mess)
        feed_pictures.append(pics)
        
    for info in json_text["events"]["data"]:
        mess=info.get('description', 'null')
        owner=info.get('name', 'null')
        start=info.get('start_time','null')
        event_description.append(mess)
        event_owner.append(owner)
        event_start.append(pics)
        
    print(feed_messages)
    print(feed_pictures)

    for i in range(len(feed_messages)):
        print(feed_messages[i])
        feed[i][0]=feed_messages[i]
        feed[i][1]=feed_pictures[i]
    
    for i in range(len(event_description)):
        event[i][0]=event_description[i]
        event[i][1]=feed_pictures[i]
    
    context = {"feed":feed,"mess": feed_messages,"pics":feed_pictures,"desc":event_description,"owner":event_owner,"start":event_start}
    return render(request, "donation/social.html", context)
    
   



