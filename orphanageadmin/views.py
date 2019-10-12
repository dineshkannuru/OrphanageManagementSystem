from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from homepage.models import Orphan
import datetime
#from .models import Post
# Create your views here.

#@login_required
def home(request):
    return render(request,'orphanageadmin/home.html')

#@login_required
def addorphan(request):
    return render(request,'orphanageadmin/addorphan.html')

#@login_required
def insertorphan(request):
    if request.method == 'POST':
        date = str(datetime.datetime.now())
        date = date.split(' ')
        date1 = date[0].split('-')
        orphan_name = request.POST['name']
        date_of_birth = request.POST['date']
        gender = request.POST['gender']
        special_skills = request.POST['spskills']
        date2 = str(date_of_birth)
        date2 = date2.split('-')
        if int(date1[0]) < int(date2[0]) or (int(date1[0]) == int(date2[0]) and int(date1[1]) < int(date2[1])) or (int(date1[0]) == int(date2[0]) and int(date1[1]) == int(date2[1]) and int(date1[2]) < int(date2[2])):
            messages.warning(request,'Error in date, Fail to add')
            return redirect('o_home')
        else:
            messages.success(request,'Added orphan successfully')
            return redirect('o_home')