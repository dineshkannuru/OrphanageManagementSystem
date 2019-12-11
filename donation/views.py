from django.shortcuts import render
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
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from homepage.models import donatemoney,donatevaluables,Orphanage,Transport, Emergency
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import MoneySerializer,testdonatemoneyserializer,testorphanageserializer,CurrentUserSerializer
import random
import pdb

# Create your views here.

@csrf_exempt
def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    print(ipn_obj)
    print("may be")
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Upgrade all users!":
            Users.objects.update(paid=True)
    else:
        Users.objects.update(paid=False)



# Create your views here.
@login_required(login_url='registration:login')
def donatemoneyview(request):
    Orphanages = Orphanage.objects.all()
    if request.method =='POST':
        user_id = request.user
        transfer = request.POST['transfer']
        amount = request.POST['amount']
        orphanage_id1 = request.POST['orphanage_id']
        orphanage=Orphanage.objects.get(pk = orphanage_id1)
        orphanage_name = orphanage.orphanage_name
        print(orphanage_id1)
        description= request.POST['description']
        status = "0"
        saveform = donatemoney.objects.create(user_id=user_id,transfer=transfer,amount=amount,orphanage_id=orphanage,orphanage_name=orphanage_name,description=description,status=status)
        saveform.save()
        tid=donatemoney.objects.latest('pk')
        print(tid)
        tidstring=tid.pk
        if transfer=="paypal":
            return HttpResponseRedirect(reverse('donation:inprogress',args=(tidstring,amount,orphanage_id1))) 
    else:
        context = {
            'orphanages': Orphanages
        }
    return render(request,'donation/money.html',context)

@csrf_exempt
def donation_completedview(request):
    args = {'post':request.POST,'get':request.GET}
    data=donatemoney.objects.latest()
    data.status='1'
    valid_ipn_received.connect(show_me_the_money)
    data.save()
    return render(request,'donation/donation_done.html',args)

@csrf_exempt
def donation_interruptview(request):
    data=donatemoney.objects.latest()
    data.status='-1'
    data.save()
    return render(request,'donation/donation_interrupt.html')

@login_required(login_url='registration:login')
def donatevaluablesview(request):
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
        return HttpResponseRedirect(reverse('donation:request_placed'))
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
    num = random.randint(1,100000)
    print(account)
    paypal_dict = {
        "business": account,
        "amount": amount,
        "currency-code":"USD",
        "item_name": num,
        "invoice": num,
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": "http://38ed8983.ngrok.io/donation/donation_done/",
        "cancel_return": "http://38ed8983.ngrok.io/donation/donation_interrupt/",
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    data=donatemoney.objects.latest()
    context = {"form": form,"data":data,"user_name":user_name,"orphanage":orphanage}
    return render(request, "donation/gatewaypage.php", context)

@csrf_exempt
def paypal_cancel(request):
    data=donatemoney.objects.latest()
    data.status='-1'
    data.save()
    return render(request,'donation/paypal_cancel.html')


#return url is mistake
@csrf_exempt
def paypal_return(request):
   data=donatemoney.objects.latest()
   data.status='1'
   valid_ipn_received.connect(show_me_the_money)
   data.save()
   return render(request,'donation/paypal_return.html')

def rejectedview(request):
    user = request.user
    rejected = donatevaluables.objects.filter(user_id=user,status=-2)
    
    context = {"rejected":rejected}
    return render(request, "donation/Rejected.html", context)


def receivedview(request):
    user = request.user
    received = donatevaluables.objects.filter(user_id=user,status=0)
    context = {"received": received}
    return render(request, "donation/received.html", context)

def acceptedview(request):
    user = request.user
    transport = Transport.objects.filter(status=0)
    accepted = donatevaluables.objects.filter(user_id=user,status=1)
    transpose=[]
    for accept in accepted:
        for trans in transport:
            if trans.danation_id == accept.pk:
                accept.status = 10
                break

    context = {"accepted": accepted,"transpose":transpose}
    return render(request, "donation/Accepted.html", context)


def historyview(request):
    user = request.user
    donations = donatemoney.objects.filter(user_id=user)
    
    context = {"donations": donations}
    return render(request, "donation/history.html", context)




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
    
   
@api_view(['GET',])
def rest_moneyview(request):

    try:
        print("1")
        donations = donatemoney.objects.all()
    except donatemoney.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = MoneySerializer(donations)
    print(serializer)
    print(serializer.data)
    return Response(serializer.data)
#
    #queryset = donatemoney.objects.all()
    #serializer_class = MoneySerializer

class testdonatemoney(viewsets.ModelViewSet):
    queryset = donatemoney.objects.all()
    serializer_class= testdonatemoneyserializer


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
    
class testorphanage(viewsets.ModelViewSet):
    queryset = Orphanage.objects.all()
    serializer_class = testorphanageserializer

@login_required(login_url='registration:login')
def emergencydonatemoneyview(request,eid):
    emergency=Emergency.objects.get(pk = eid)
    print(emergency)
    Orphanages = emergency.orphanage_id
    des = emergency.situation
    des = str(des)
    print(Orphanages)
   # des = emergency.situation
   # Orphanages=Orphanage.objects.get(pk = id_orphanage)
    if request.method =='POST':
        user_id = request.user
        transfer = request.POST['transfer']
        amount = request.POST['amount']
        orphanage_id1 = request.POST['orphanage_id']
        orphanage=Orphanage.objects.get(pk = orphanage_id1)
        orphanage_name = orphanage.orphanage_name
        print(orphanage_id1)
        description= des
        paypal_transaction = 'None'
        status = "0"
        saveform = donatemoney.objects.create(user_id=user_id,transfer=transfer,amount=amount,orphanage_id=orphanage,orphanage_name=orphanage_name,description=description,status=status,paypal_transaction= paypal_transaction)
        saveform.save()
        tid=donatemoney.objects.latest('pk')
        print(tid)
        tidstring=tid.pk
        if transfer=="paypal":
            return HttpResponseRedirect(reverse('donation:inprogress',args=(tidstring,amount,orphanage_id1)))
    else:
        context = {
            'orphanage': Orphanages,'des':des
        }
    return render(request,'donation/emer_donate.html',context)



valid_ipn_received.connect(show_me_the_money)

