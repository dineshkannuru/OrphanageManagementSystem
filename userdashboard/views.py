from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from homepage.models import Orphan,Orphanage,donatevaluables,donatemoney,Emergency,Events,Orphan,UserDetails,AddOrphan

@login_required
def Profile(request):
    user = request.user
    print(user)
    qs = User.objects.get(username=user)
    qs1=UserDetails.objects.get(user_id=qs)
    #content = {'orphanage_name':orphanage.orphanage_name}
    #print(qs.first_name,qs.last_name,qs.email)
    return render(request,'userdashboard/profile.html',{"qs":qs,"qs1":qs1})

@login_required
def profileupdate(request):
    user = request.user
    print(user)
    qs = User.objects.get(username=user)
    qs1=UserDetails.objects.get(user_id=qs)
    #content = {'orphanage_name':orphanage.orphanage_name}
    #print(qs.first_name,qs.last_name,qs.email)
    return render(request,'userdashboard/edit_profile.html',{"qs":qs,"qs1":qs1})

@login_required
def editprofile(request):
    if request.method == 'POST':
        user = request.user
        print(user)
        empty=''
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        phone_no=request.POST['phone_no']
        email=request.POST['email']
        #address=request.POST['address']
        qs = User.objects.get(username=user)
        qs1 = UserDetails.objects.get(user_id=qs)
        if first_name ==empty:
            pass
        else:
            qs.first_name=first_name

        if last_name ==empty:
            pass
        else:
            qs.last_name=last_name

        if phone_no ==empty:
            pass
        else:
            qs1.phone_no=phone_no
        if email ==empty:
            pass
        else:
            qs.email=email
        qs.save()
        qs1.save()
        qs = User.objects.get(username=user)
        qs1 = UserDetails.objects.get(user_id=qs)
        # content = {'orphanage_name':orphanage.orphanage_name}
        # print(qs.first_name,qs.last_name,qs.email)
        return render(request, 'userdashboard/profile.html', {"qs": qs, "qs1": qs1})

def requestJoinOrphan(request):
    if request.method == "POST":
        print('orp=')
        print(request.POST['orphanage'])
        joinorphan_request = AddOrphan.objects.create(
         user_id=request.user,
         orphanage_id= Orphanage.objects.get(orphanage_name=request.POST['orphanage']),
         name=request.POST['name'],
         gender=request.POST['gender'],
         find_place=request.POST['find_place'],
         ref_no=0,
         date_of_birth=request.POST['DOB']
        )
        joinorphan_request.save()
        all_orphanages = Orphanage.objects.all()
        all_orphanages_list = []
        for item in all_orphanages:
            print(item.orphanage_name)
            all_orphanages_list.append(item.orphanage_name)
        messages.success(request, 'Your request to join an orphan has been sent, it will be verified soon.')
        return render(request, 'userdashboard/request_joinorphan.html',
                      {'orphanages': all_orphanages_list})
    else:
        all_orphanages = Orphanage.objects.all()
        all_orphanages_list = []
        for item in all_orphanages:
            all_orphanages_list.append(item.orphanage_name)
        return render(request, 'userdashboard/request_joinorphan.html', {'orphanages': all_orphanages_list})

def acceptedJoinOrphan_requests(request):
    accepted_joinorphan_requests = AddOrphan.objects.filter(ref_no=1, user_id=request.user)
    return render(request, 'userdashboard/accepted_joinorphan_request.html',{'accepted_requests': accepted_joinorphan_requests})

def rejectedJoinOrphan_requests(request):
    rejected_joinorphan_requests = AddOrphan.objects.filter(ref_no=-1, user_id=request.user)
    return render(request, 'userdashboard/rejected_joinorphan_request.html', {'rejected_requests': rejected_joinorphan_requests})

def pendingJoinOrphan_requests(request):
    pending_joinorphan_requests = AddOrphan.objects.filter(ref_no=0, user_id=request.user)
    return render(request, 'userdashboard/pending_joinorphan_request.html',
                  {'pending_requests': pending_joinorphan_requests})
