from django.shortcuts import render
from .models import Orphanage,donatevaluables,UserDetails,Transport
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
# Create your views here.
def index(request):
    return render(request,'homepage/index.html')
def index1(request):
    return render(request,'homepage/contact.html')


class followview(APIView):

    def get(self,request):

        data=Orphanage.objects.filter(status='Freshly Applied')
        list1=[]
        for each in data:
            
            var={
                'orphanage_id':each.orphanage_id.pk,
                'orphanage_name':each.orphanage_name,
                'year_of_establishment':each.year_of_establishment,
                #'log':each.lon,
                #'lat':each.lat,
                'address':each.address,
                'phone_no': each.phone_no,
                #'image': each.image,
                'description': each.description
            }
            list1.append(var)
        return Response(list1)
class followview1(APIView):
    def post(self, request):
        print('came to eoor')
        print(request.data)
        for each in request.data:
            print('eacho='+str(request.data[each]['orphanage_id']))
            print('jii')
            orphanage_id = request.data[each]['orphanage_id']
            status1 = request.data[each]['status']
            print(orphanage_id,status1)
            print('came')
            for i in Orphanage.objects.all():
                print('id='+str(i.orphanage_id))
            print('gone')
            orp = Orphanage.objects.get(orphanage_id=int(orphanage_id))
            user1=User.objects.filter(user=orp.orphanage_id)
            print(user1.username)
            if status1=='Accepted':
                orp.status='Accepted'

                orp.save()
            else:
                print('deletecame')
                orp.status='Rejected'
                orp.save()   
            
            
            
            print('orpcompl')
            print(s)
            
            print('cametoend')
                








class transport(APIView):
    def get(self,request):
        data=donatevaluables.objects.filter(status=0) #0 means not delivered
        list1=[]
        for each in data:
            z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
            print(z)
            h =User.objects.get(id=each.user_id.id)
            print(h.id,h.username)
            h1=UserDetails.objects.get(user_id=h.id)
            var={
                'donation_id':each.pk,
                'orphanage_name':each.orphanage_id.orphanage_name,
                'user_name':each.user_id.username,
                'donation_type':each.donation_type,
                'quantity':each.quantity,
                #'orphanage_name':each.orphanage_name,
                #'year_of_establishment':each.year_of_establishment,
                #'log':each.lon,
                #'lat':each.lat,
                'address':z.address,
                'phone_no': z.phone_no,
                'phone_no_user': h1.phone_no,
                #'image': each.image,
                #'description': each.description,
                #'status':each.status
            }
            list1.append(var)
        return Response(list1)

class transportid(APIView):
    def get(self,request,id):
        #data=Donation.objects.filter(status=0) #0 means not delivered
        list1=[]

        each=donatevaluables.objects.get(status=0,pk=id) #0 means not delivered
        z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
        h=User.objects.get(id=each.user_id.id)
        h1=UserDetails.objects.get(user_id=h.id)
        var={
            'donation_id':each.pk,
            'orphanage_name':each.orphanage_id.orphanage_name,
            'user_name':each.user_id.username,
            'donation_type':each.donation_type,
            'quantity':each.quantity,
            #'orphanage_name':each.orphanage_name,
            #'year_of_establishment':each.year_of_establishment,
            #'log':each.lon,
            #'lat':each.lat,
            'address':z.address,
            'phone_no': z.phone_no,
            'phone_no_user': h1.phone_no,
            #'image': each.image,
            #'description': each.description,
            #'status':each.status
        }

        list1.append(var)
        return Response(list1)


class transport2(APIView):
    def get(self,request,company_name):
        data=Transport.objects.all()
        list=[]
        status="Not Checked "
        for each in data:
            print(each.status)
            if each.status=='1': #1 means Accepted
                status="Accepted"
            elif each.status=='2':#2 means Rejected
                status="Rejected"
            var={
            'donation_id':each.danation_id,
            'status':status
            }
            print(each.company_name)
            if each.company_name==company_name:
                list.append(var)
        return Response(list)

class transport1(APIView):
    def post(self, request):
        print(request.data)
        for each in request.data:
            danation_id=request.data[each]['donation_id']
            type = request.data[each]['Type']
            cost = request.data[each]['cost']
            duration=request.data[each]['duration']
            company_name=request.data[each]['company_name']
            print(type,cost,duration,company_name,danation_id)
            #h=Donation.objects.get(pk=danation_id)
            data=Transport.objects.filter(danation_id=danation_id)
            count=0
            for k in data:
                print(k.company_name,company_name)
                if k and k.company_name==company_name :
                    count=count+1
            print(count)
            if count==0:
                newtransport=Transport.objects.create(
                danation_id=danation_id,
                type=type,
                duration=duration,
                company_name=company_name,
                cost=cost
                )
                newtransport.save()
