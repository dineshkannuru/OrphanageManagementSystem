from django.shortcuts import render
from .models import Orphanage,donatevaluables,UserDetails,Transport,verification,Type,Events,catering
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.utils import timezone
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import datetime
from datetime import date
from rest_framework.authtoken.models import Token

# Create your views here.
# Create your views here.
def index(request):
    return render(request,'homepage/index.html')
def index1(request):
    return render(request,'homepage/contact.html')

class gettoken(APIView):
    def get(self,request,company_name,password):
        k=verification.objects.filter(companyname=company_name ,  password=password)
        print(k)
        list1=[]
        if len(k)!=0:
            var={
                'token':k[0].token
            }
            list1.append(var)
        else :
            var={
                'error':"Incorrect UserName,Password"
            }
            list1.append(var)
        return Response(list1)


class followview(APIView):
    def get(self,request,company_name):
        list1 = []
        f=verification.objects.filter(token=company_name)
        if len(f)!=0:
            time=datetime.datetime.now()
            b=(f[0].hit)

            data=Orphanage.objects.filter(status='Freshly Applied')
            for each in data:
                var={
                    'orphanage_id':each.orphanage_id.pk,
                    'orphanage_name':each.orphanage_name,
                    'year_of_establishment':each.year_of_establishment,
                    #'log':each.lon,
                    #'lat':each.lat,
                    'address':each.address,
                    'phone_no': each.phone_no,
                    'lat':each.lat,
                    'lon':each.lon,
                    #'image': each.image,
                    'description': each.description
                }
                list1.append(var)

        else:
            var={"detail": "Authentication credentials were not provided."}
            list1.append(var)
        return Response(list1)


class followview1(APIView):
    def post(self, request,company_name):
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            time = datetime.datetime.now()
            b = (f[0].hit)

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
                print('name=',end=' ')
                print(orp.orphanage_id.username)
                a=User.objects.get(username=orp.orphanage_id.username)
                print(a.username)
                b=Type.objects.get(user=a)
                print('cametorequired')


                if status1=='Accepted':
                    b.ref_no=3
                    orp.status='Accepted'
                    orp.save()
                    b.save()
                else:
                    print('deletecame')
                    b.ref_no=0
                    orp.status='Rejected'
                    orp.save()
                    b.save()
            

            print('orpcompl')

            print('cametoend')
        else:
            list1=[]
            var={"detail": "Authentication credentials were not provided."}
            list1.append(var)
            return Response(list1)

class transportuser(APIView):
    def get(self,request,company_name):
        data=donatevaluables.objects.filter(status=1) #1 admin accepted
        list1=[]
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            time = datetime.datetime.now()
            b = (f[0].hit)
            if abs(time.second - b.second) > 5:
                f[0].hit = datetime.datetime.now()
                f[0].save()

                for each in data:
                    z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
                    print(z)
                    h =User.objects.get(id=each.user_id.id)
                    print(h.id,h.username)
                    h1=UserDetails.objects.get(user_id=h.id)
                    var={
                        'donation_id':each.pk,
                        'orphanage_id':each.orphanage_id.orphanage_name,
                        'user_id':each.user_id.username,
                        'donation_type':each.donation_type,
                        'quantity':each.quantity,
                        #'orphanage_name':each.orphanage_name,
                        #'year_of_establishment':each.year_of_establishment,
                        #'log':each.lon,
                        #'lat':each.lat,
                        'address':z.address,
                        'phone_no': z.phone_no,
                        'phone_no_user': h1.phone_no,
                        'address_user':each.address,
                        #'image': each.image,
                        #'description': each.description,
                        #'status':each.status
                    }
                    list1.append(var)

            else :
                list1 = []
                var = {"detail": "Hit after five seconds"}
                list1.append(var)


        else:
            var={"detail": "Authentication credentials were not provided."}
            list1.append(var)
        return Response(list1)

class transportuserid(APIView):
    def get(self,request,id,company_name):
        #data=Donation.objects.filter(status=0) #1 admin accepted
        list1=[]
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            time = datetime.datetime.now()
            b = (f[0].hit)
        
            each=donatevaluables.objects.get(status=1,pk=id) #1 admin accepted
            z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
            h=User.objects.get(id=each.user_id.id)
            h1=UserDetails.objects.get(user_id=h.id)
            var={
                'donation_id':each.pk,
                'orphanage_id':each.orphanage_id.orphanage_name,
                'user_id':each.user_id.username,
                'donation_type':each.donation_type,
                'quantity':each.quantity,
                #'orphanage_name':each.orphanage_name,
                #'year_of_establishment':each.year_of_establishment,
                #'log':each.lon,
                #'lat':each.lat,
                'address':z.address,
                'phone_no': z.phone_no,
                'phone_no_user': h1.phone_no,
                'address_user': each.address,
                #'image': each.image,
                #'description': each.description,
                #'status':each.status
            }

            list1.append(var)


        else:
            var={"detail": "Authentication credentials were not provided."}
            list1.append(var)
        return Response(list1)


class useraccepted(APIView):
    def get(self,request,company_name):
        k=verification.objects.filter(token=company_name)
        list = []
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            company_name=k[0].companyname.company_name
            data=Transport.objects.all()

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

        else:
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
        return Response(list)


class transporttoken(APIView):
    def post(self, request,company_name):
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            time = datetime.datetime.now()
            b = (f[0].hit)

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
                    newtransport=Transport.objects.create(   #creating object
                    danation_id=danation_id,
                    type=type,
                    duration=duration,
                    company_name=company_name,
                    cost=cost,
                    status='0'
                    )
                    newtransport.save()

        else:
            list=[]
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
            return Response(list)






class useracceptedid(APIView):
    def get(self,request,id,company_name):
        k=verification.objects.filter(token=company_name)
        list = []
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:

            f[0].hit = datetime.datetime.now()
            f[0].save()
            company_name=k[0].companyname.company_name
            data=Transport.objects.filter(danation_id=id)

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

        else:
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
        return Response(list)

class transport4(APIView):
    def get(self,request,id,company_name):
        k=verification.objects.filter(token=company_name)
        list = []
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            time = datetime.datetime.now()
            b = (f[0].hit)

            company_name=k[0].companyname
            data=Transport.objects.filter(danation_id=id)
            status="Not delivered"
            for each in data:
                print(each.status)
                if each.status=='3': #1 means Accepted
                    status="delivered"
                elif each.status=='1':#2 means Rejected
                    status="Not delivered"
                var={
                'donation_id':each.danation_id,
                'status':status,
                'date':date.today()
                }
                print(each.company_name)
                if each.company_name==company_name.company_name:
                    list.append(var)

        else:
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
        return Response(list)




#---------------------------------------------------------------------------------------------#

class usercatering(APIView):
    def get(self,request,company_name):
        k = verification.objects.filter(token=company_name)
        list = []
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            time = datetime.datetime.now()
            b = (f[0].hit)
            if abs(time.second - b.second) > 5:
                f[0].hit = datetime.datetime.now()
                f[0].save()
                data=Events.objects.filter(status='Accepted') # admin accepted
                print(data)
                for each in data:
                    z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
                    print(z)
                    h =User.objects.get(id=each.user_id.id)
                    print(h.id,h.username)
                    h1=UserDetails.objects.get(user_id=h.id)
                    var={
                    'date_of_event':each.date_of_event,
                    'event':each.event,
                    'username':each.user_id.username,
                    'orphanage_name':each.orphanage_id.orphanage_name,
                    'description':each.description,
                    'user_phonenumber':h1.phone_no,
                    'orphanage_phonenumber':z.phone_no,
                    'address':z.address,
                    'id':each.pk


                    }
                    list.append(var)
            else :

                var = {"detail": "Hit after five seconds"}
                list.append(var)


        else:
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
        return Response(list)






class usercateringid(APIView):
    def get(self,request,id,company_name):
        k = verification.objects.filter(token=company_name)
        list = []
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            # time = datetime.datetime.now()
            # b = (f[0].hit)
            # if abs(time.second - b.second) > 5:
            #     f[0].hit = datetime.datetime.now()
            #     f[0].save()
            each=Events.objects.get(status='Accepted',pk=id) # admin accepted
            z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
            print(z)
            h =User.objects.get(id=each.user_id.id)
            print(h.id,h.username)
            h1=UserDetails.objects.get(user_id=h.id)
            var={
                'date_of_event':each.date_of_event,
                'event':each.event,
                'username':each.user_id.username,
                'orphanage_name':each.orphanage_id.orphanage_name,
                'description':each.description,
                'user_phonenumber':h1.phone_no,
                'orphanage_phonenumber':z.phone_no,
                'address':z.address,
                'id':each.pk

            }
            list.append(var)
            # else :
            #
            #     var = {"detail": "Hit after five seconds"}
            #     list.append(var)

        else:
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
        return Response(list)





class cateringtoken(APIView):
    def post(self, request,company_name):
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            # time = datetime.datetime.now()
            # b = (f[0].hit)
            # if abs(time.second - b.second) > 5:
            #     f[0].hit = datetime.datetime.now()
            #     f[0].save()

            print(request.data)
            for each in request.data:
                event_id=request.data[each]['event_id']           #request.data[each]['event_id']
                company_name=request.data[each]['company_name']   #request.data[each]['company_name']
                items=request.data[each]['items']                     #request.data[each]['description']
                price=request.data[each]['price']
                image=request.data[each]['image']
                print(company_name,event_id,image,items,price)
                #h=Donation.objects.get(pk=danation_id)
                data=catering.objects.filter(event_id=event_id)
                count=0
                for k in data:
                    print(k.company_name,company_name)
                    if k and k.company_name==company_name :
                        count=count+1
                print(count)
                if count==0:
                    newtransport=catering.objects.create(   #creating object
                    event_id=event_id,
                    company_name=company_name,
                    items=items,
                    price=price,
                    image=image,
                    status='0'
                    )
                    newtransport.save()
            # else :
            #     list=[]
            #     var = {"detail": "Hit after five seconds"}
            #     list.append(var)

        else:
            list=[]
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
            return Response(list)





class useracceptcateringid(APIView):
    def get(self,request,id,company_name):
        k=verification.objects.filter(token=company_name)
        list = []
        f = verification.objects.filter(token=company_name)
        if len(f) != 0:
            time = datetime.datetime.now()
            b = (f[0].hit)
            if abs(time.second - b.second) > 5:
                f[0].hit = datetime.datetime.now()
                f[0].save()
                company_name=k[0].companyname
                data=catering.objects.filter(event_id=id)
                print('hii')
                status="Not Checked "
                for each in data:
                    print(each.status)
                    if each.status=='1': #1 means Accepted
                        status="Accepted"
                    elif each.status=='2':#2 means Rejected
                        status="Rejected"
                    var={
                    'donation_id':each.event_id,
                    'status':status
                    }
                    if each.company_name==company_name.company_name:
                        list.append(var)
            else :

                var = {"detail": "Hit after five seconds"}
                list.append(var)

        else:
            var={"detail": "Authentication credentials were not provided."}
            list.append(var)
        return Response(list)









#class transport(APIView):
#    def get(self,request,company_name):
#        data=donatevaluables.objects.filter(status=0) #0 means not delivered
#        list1=[]
#        if len(verification.objects.filter(token=company_name)) != 0:
#            for each in data:
#                z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
#                print(z)
#                h =User.objects.get(id=each.user_id.id)
#                print(h.id,h.username)
#                h1=UserDetails.objects.get(user_id=h.id)
#                var={
#                    'donation_id':each.pk,
#                    'orphanage_id':each.orphanage_id.orphanage_name,
#                    'user_id':each.user_id.username,
#                    'donation_type':each.donation_type,
#                    'quantity':each.quantity,
#                    #'orphanage_name':each.orphanage_name,
#                    #'year_of_establishment':each.year_of_establishment,
#                    #'log':each.lon,
#                    #'lat':each.lat,
#                    'address':z.address,
#                    'phone_no': z.phone_no,
#                    'phone_no_user': h1.phone_no,
#                    'address_user':"Chennai",
#                    #'image': each.image,
#                    #'description': each.description,
#                    #'status':each.status
#                }
#                list1.append(var)
#        else:
#            var={"detail": "Authentication credentials were not provided."}
#            list1.append(var)
#        return Response(list1)
#
#class transportid(APIView):
#    def get(self,request,id,company_name):
#        #data=Donation.objects.filter(status=0) #0 means not delivered
#        list1=[]
#        if len(verification.objects.filter(token=company_name)) != 0:
#
#            each=donatevaluables.objects.get(status=0,pk=id) #0 means not delivered
#            z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
#            h=User.objects.get(id=each.user_id.id)
#            h1=UserDetails.objects.get(user_id=h.id)
#            var={
#                'donation_id':each.pk,
#                'orphanage_id':each.orphanage_id.orphanage_name,
#                'user_id':each.user_id.username,
#                'donation_type':each.donation_type,
#                'quantity':each.quantity,
#                #'orphanage_name':each.orphanage_name,
#                #'year_of_establishment':each.year_of_establishment,
#                #'log':each.lon,
#                #'lat':each.lat,
#                'address':z.address,
#                'phone_no': z.phone_no,
#                'phone_no_user': h1.phone_no,
#                'address_user': "Chennai",
#                #'image': each.image,
#                #'description': each.description,
#                #'status':each.status
#            }
#
#            list1.append(var)
#        else:
#            var={"detail": "Authentication credentials were not provided."}
#            list1.append(var)
#        return Response(list1)
#
#
#class transport2(APIView):
#    def get(self,request,company_name):
#        k=verification.objects.filter(token=company_name)
#        list = []
#        if len(k) != 0:
#            company_name=k[0].companyname
#            data=Transport.objects.all()
#
#            status="Not Checked "
#            for each in data:
#                print(each.status)
#                if each.status=='1': #1 means Accepted
#                    status="Accepted"
#                elif each.status=='2':#2 means Rejected
#                    status="Rejected"
#                var={
#                'donation_id':each.danation_id,
#                'status':status
#                }
#                print(each.company_name)
#                if each.company_name==company_name:
#                    list.append(var)
#        else:
#            var={"detail": "Authentication credentials were not provided."}
#            list.append(var)
#        return Response(list)
#
#
#class transport1(APIView):
#    def post(self, request,company_name):
#        if len(verification.objects.filter(token=company_name)) != 0:
#
#            print(request.data)
#            for each in request.data:
#                danation_id=request.data[each]['donation_id']
#                type = request.data[each]['Type']
#                cost = request.data[each]['cost']
#                duration=request.data[each]['duration']
#                company_name=request.data[each]['company_name']
#                print(type,cost,duration,company_name,danation_id)
#                #h=Donation.objects.get(pk=danation_id)
#                data=Transport.objects.filter(danation_id=danation_id)
#                count=0
#                for k in data:
#                    print(k.company_name,company_name)
#                    if k and k.company_name==company_name :
#                        count=count+1
#                print(count)
#                if count==0:
#                    newtransport=Transport.objects.create(   #creating object
#                    danation_id=danation_id,
#                    type=type,
#                    duration=duration,
#                    company_name=company_name,
#                    cost=cost
#                    )
#                    newtransport.save()
#        else:
#            list=[]
#            var={"detail": "Authentication credentials were not provided."}
#            list.append(var)
#            return Response(list)
#
#class transport3(APIView):
#    def get(self,request,id,company_name):
#        k=verification.objects.filter(token=company_name)
#        list = []
#        if len(k) != 0:
#            company_name=k[0].companyname
#            data=Transport.objects.filter(danation_id=id)
#
#            status="Not Checked "
#            for each in data:
#                print(each.status)
#                if each.status=='1': #1 means Accepted
#                    status="Accepted"
#                elif each.status=='2':#2 means Rejected
#                    status="Rejected"
#                var={
#                'donation_id':each.danation_id,
#                'status':status
#                }
#                print(each.company_name)
#                if each.company_name==company_name:
#                    list.append(var)
#        else:
#            var={"detail": "Authentication credentials were not provided."}
#            list.append(var)
#
#        return Response(list)
#
#
#
# class transport(APIView):
#     def get(self,request):
#         data=donatevaluables.objects.filter(status=0) #0 means not delivered
#         list1=[]
#         for each in data:
#             z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
#             print(z)
#             h =User.objects.get(id=each.user_id.id)
#             print(h.id,h.username)
#             h1=UserDetails.objects.get(user_id=h.id)
#             var={
#                 'donation_id':each.pk,
#                 'orphanage_name':each.orphanage_id.orphanage_name,
#                 'user_name':each.user_id.username,
#                 'donation_type':each.donation_type,
#                 'quantity':each.quantity,
#                 #'orphanage_name':each.orphanage_name,
#                 #'year_of_establishment':each.year_of_establishment,
#                 #'log':each.lon,
#                 #'lat':each.lat,
#                 'address':z.address,
#                 'phone_no': z.phone_no,
#                 'phone_no_user': h1.phone_no,
#                 #'image': each.image,
#                 #'description': each.description,
#                 #'status':each.status
#             }
#             list1.append(var)
#         return Response(list1)
#
# class transportid(APIView):
#     def get(self,request,id):
#         #data=Donation.objects.filter(status=0) #0 means not delivered
#         list1=[]
#
#         each=donatevaluables.objects.get(status=0,pk=id) #0 means not delivered
#         z = Orphanage.objects.get(orphanage_id=each.orphanage_id.orphanage_id)
#         h=User.objects.get(id=each.user_id.id)
#         h1=UserDetails.objects.get(user_id=h.id)
#         var={
#             'donation_id':each.pk,
#             'orphanage_name':each.orphanage_id.orphanage_name,
#             'user_name':each.user_id.username,
#             'donation_type':each.donation_type,
#             'quantity':each.quantity,
#             #'orphanage_name':each.orphanage_name,
#             #'year_of_establishment':each.year_of_establishment,
#             #'log':each.lon,
#             #'lat':each.lat,
#             'address':z.address,
#             'phone_no': z.phone_no,
#             'phone_no_user': h1.phone_no,
#             #'image': each.image,
#             #'description': each.description,
#             #'status':each.status
#         }
#
#         list1.append(var)
#         return Response(list1)
#
#
# class transport2(APIView):
#     def get(self,request,company_name):
#         data=Transport.objects.all()
#         list=[]
#         status="Not Checked "
#         for each in data:
#             print(each.status)
#             if each.status=='1': #1 means Accepted
#                 status="Accepted"
#             elif each.status=='2':#2 means Rejected
#                 status="Rejected"
#             var={
#             'donation_id':each.danation_id,
#             'status':status
#             }
#             print(each.company_name)
#             if each.company_name==company_name:
#                 list.append(var)
#         return Response(list)
#
# class transport1(APIView):
#     def post(self, request):
#         print(request.data)
#         for each in request.data:
#             danation_id=request.data[each]['donation_id']
#             type = request.data[each]['Type']
#             cost = request.data[each]['cost']
#             duration=request.data[each]['duration']
#             company_name=request.data[each]['company_name']
#             print(type,cost,duration,company_name,danation_id)
#             #h=Donation.objects.get(pk=danation_id)
#             data=Transport.objects.filter(danation_id=danation_id)
#             count=0
#             for k in data:
#                 print(k.company_name,company_name)
#                 if k and k.company_name==company_name :
#                     count=count+1
#             print(count)
#             if count==0:
#                 newtransport=Transport.objects.create(
#                 danation_id=danation_id,
#                 type=type,
#                 duration=duration,
#                 company_name=company_name,
#                 cost=cost
#                 )
#                 newtransport.save()
