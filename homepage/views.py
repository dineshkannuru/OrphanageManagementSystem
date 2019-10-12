from django.shortcuts import render
from .models import Orphanage
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
        data=Orphanage.objects.all()
        list1=[]
        for each in data:
            var={
                'orphanage_id':each.orphanage_id,
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

