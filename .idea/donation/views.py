from django.shortcuts import render
import json
import re
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
from homepage.models import donatemoney,donatevaluables,Orphanage,Transport,Emergency
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
        paypal_transaction = 'None'
        status = "0"
        saveform = donatemoney.objects.create(user_id=user_id,transfer=transfer,amount=amount,orphanage_id=orphanage,orphanage_name=orphanage_name,description=description,status=status,paypal_transaction= paypal_transaction)
        try:
            saveform.save()
        except:
            print("ERROR")
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


@login_required(login_url='registration:login')
def emergencydonatemoneyview(request,eid):
    emergency=Emergency.objects.get(pk = eid)
    print(emergency)
    Orphanages = emergency.orphanage_id
    des = emergency.situation
    des=str(des)
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
        description = des
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


@csrf_exempt
def donation_completedview(request):
    return render(request,'donation/donation_done.html')

@csrf_exempt
def donation_interruptview(request):
    return render(request,'donation/donation_interrupt.html')

@login_required(login_url='registration:login')
def donatevaluablesview(request):
    Orphanages = Orphanage.objects.all()
    if request.method =='POST':
        user_id = request.user
        type =request.POST.get('type')
        quantity=request.POST.get('quantity')
        orphanage_id1 = request.POST['orphanage_id']
        orphanage=Orphanage.objects.get(pk = orphanage_id1)
        orphanage_name = orphanage.orphanage_name
        object = request.POST.get('object_name')
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
    print(account)
    paypal_dict = {
        "business": account,
        "amount": amount,
        "currency-code":"USD",
        "item_name": amount,
        "invoice": tid,
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": "http://3c11fa0e.ngrok.io/donation/donation_done/",
        "cancel_return": "http://3c11fa0e.ngrok.io/donation/donation_interrupt/",
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
    transport1 = Transport.objects.filter(status=1)

    accepted = donatevaluables.objects.filter(user_id=user,status=1)
    accepted12 = donatevaluables.objects.filter(user_id=user,status=2)
    accepted=accepted.union(accepted12)
    transpose=[]
    for accept in accepted:
        for trans in transport:
            if trans.danation_id == accept.pk:
                accept.status = 10
                break
    context = {"accepted": accepted,"transpose":transpose,"transport1":transport1}
    return render(request, "donation/Accepted.html", context)


def historyview(request):
    user = request.user
    donations = donatemoney.objects.filter(user_id=user)
    count=0
    badge=0
    for donation in donations:
        if donation.status ==2:
            count += donation.amount
            if count>250:
                badge=25
            elif count>500:
                badge=50
            elif count>1000:
                badge=100
            else:
                badge=0
    badge=str(badge)
    print(badge)
    print(count)
    if count<1000:
        percent = count/1000*100
    else:
        percent = 100
    
    context = {"donations": donations,'badge':badge,'count':count,'percent':percent}
    return render(request, "donation/test2.html", context)


def progressview(request):
    user = request.user
    donations = donatemoney.objects.filter(user_id = user)
    count=0
    badge=0
    for donation in donations:
        if donation.paypal_transaction !=None:
            count += donation.amount
            if count>25:
                badge=1
            elif count>50:
                badge=2
            elif count>100:
                badge=3
            else:
                badge=4

    context = {'badge':badge,'count':count}
    return render(request, "donation/progress.html", context)

#COULD not access 2d list in django
def socialview(request):
    url= "https://graph.facebook.com/v5.0/107316914058945?fields=posts.limit(20)%7Bmessage%2Cfrom%2Cadmin_creator%2Cfull_picture%2Ccreated_time%2Clikes.summary(true)%2Cplace%2Cevent%2Cid%7D%2Cevents.limit(10)%7Bowner%2Cdescription%2Cstart_time%2Cname%2Cend_time%2Cpicture%7D&transport=cors&access_token=EAALOtHuxZAWUBAPYBI0QoZAcslh0gA6TpBi4O47az8CWDA2g4ipZCoeD3Ve4ZCblC1z8jaDk08JVZAmW0c8vHh8Bt4u6iKZAlItfdkaFEbFf8M7mLLKg1keoSNAJ8jOfJ1Sny4ZBOUuEpsOEN6UFdOa3U4wX8xTwN6D7IBh91i01ZBBEZBvwKx3Wg9Nfcb95dO08ZD"
    response=urlopen(url)
    json_text = load(response)
    
    feed_messages=list()
    feed_pictures=list()
    feed_date=list()
    event_owner=list()
    event_description=list()
    event_start=list()
    event_iden=list()
    event_end=list()
    event_pics=list()
    event_title=list()
    feed_likes = list()
    event_time=list()
    feed=list()
    event=list()
   
    date=''
    iden_list=[]
    start=[]

        
    for info in json_text["events"]["data"]:
        start_list=[]
        date_list=[]
        end_list=[]
        mess=info.get('description',None)
        owner=info['owner'].get('name', None)
        title=info.get('name', None)
        start=info.get('start_time',None)
        start_list=re.split(r'T',start)
        print(start_list[1])
        p=str(start_list[1])
        date_list=re.split(r':',p)
        start = str(start_list[0])
        time=str(date_list[0])+str(':')+str(date_list[1])
        end=info.get('end_time', None)
        end_list=re.split(r'T',end)
        print(end_list[1])
        p=str(end_list[1])
        end_list=re.split(r':',p)
        end=str(end_list[0])+str(':')+str(end_list[1])
        pics=info.get('full_picture',None)
        iden=info.get('id',None)
        event_description.append(mess)
        event_owner.append(owner)
        event_pics.append(pics)
        event_title.append(title)
        event_start.append(start)
        event_end.append(end)
        event_iden.append(iden)
        event_time.append(time)  
        

    for info in json_text["posts"]["data"]:
        mess=info.get('message', None)
        pics=info.get('full_picture',None)
        iden=info.get('id',None)
        iden_list = re.split(r'_',iden)
        iden=iden_list[1]
        if iden not in event_iden: 
            count = info['likes']['summary']['total_count']
            if count !=0:
                likes = count
            else:
                likes = None
            date=str((info.get('created_time',None)))
            date = re.split(r'T',date)
            print(date)
            feed_messages.append(mess)
            feed_pictures.append(pics)
            feed_likes.append(likes)
            feed_date.append(date[0])
            
    print(feed_messages)
    print(feed_pictures)

    for i in range(len(feed_messages)):
        print(feed_messages[i])
        feed.append([i,feed_messages[i],feed_pictures[i],feed_likes[i],feed_date[i]])
    
    for i in range(len(event_description)):
        event.append([i,event_title[i],event_description[i],event_pics[i],event_owner[i],event_start[i],event_time[i],event_end[i]])
    
    context = {"feed":feed,"mess": feed_messages,"pics":feed_pictures,"desc":event_description,"owner":event_owner,"start":event_start,'events':event}
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
