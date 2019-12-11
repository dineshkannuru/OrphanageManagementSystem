from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from homepage.models import Orphan,Orphanage,donatevaluables,donatemoney,Emergency,Events,Orphan,AddOrphan,Transport
import datetime
import json


@login_required
def Profile(request):
    user = request.user
    print(user)
    qs = Orphanage.objects.get(orphanage_id = user)
    qs1=User.objects.get(username=user)
    #content = {'orphanage_name':orphanage.orphanage_name}
    print(qs.image,'###')
    return render(request,'orphanageadmin/profile.html',{"qs":qs,"qs1":qs1})

@login_required
def result1(request):
    user = request.user
    print(user)
    qs = Orphanage.objects.get(orphanage_id = user)
    qs1=User.objects.get(username=user)

    #content = {'orphanage_name':orphanage.orphanage_name}
    print(qs.orphanage_name)
    return render(request,'orphanageadmin/edit_profile.html',{"qs":qs,"qs1":qs1})

@login_required
def result(request):
    if request.method == 'POST':
        user = request.user
        print(user)
        empty=''
        qs = Orphanage.objects.get(orphanage_id = user)
        qs1=User.objects.get(username=user)

        orphanage_name=request.POST.get('orphanage_name')
        phone_no=request.POST.get('phone_no')
        year_of_establishment=request.POST.get('year_of_establishment')
        description=request.POST.get('description')
        address=request.POST.get('address')
        email=request.POST.get('email')
        print(orphanage_name)
        print(phone_no)
        print(year_of_establishment)
        print(description)
        print(address)

        
        if email==empty:
            pass
        else:
            qs1.email = email

        if phone_no==empty:
            pass
        else:
            qs.phone_no = phone_no

        if year_of_establishment == empty:
            pass
        else:
            qs.year_of_establishment = year_of_establishment
        if description == empty:
            pass
        else:
            qs.description = description

        if address == empty:
            pass
        else:
            qs.address = address



        qs1.save()
        qs.save()
        qs1=User.objects.get(username=user)
        qs = Orphanage.objects.get(orphanage_id=user)
        return render(request,'orphanageadmin/profile.html',{"qs":qs,"qs1":qs1})

@login_required
def RequestedDonations(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = donatevaluables.objects.filter(orphanage_id = orphanage , status = 0)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/requested_donations.html',content)

@login_required
def RequestedDonationsAccRej(request):
    if request.method == 'POST':
        val = int(request.POST["val"])
        id1 = request.POST["id1"]
        donatevaluables.objects.filter( tid = id1).update(status = val)
        print(val)
        if val == 1:
            messages.success(request,'Successfully accepted the request')
            return redirect('orphanageadmin:o_requesteddonations')
        else:
            messages.warning(request,'Successfully rejected the request')
            return redirect('orphanageadmin:o_requesteddonations')

@login_required
def AcceptedDonations(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = donatevaluables.objects.filter(orphanage_id = orphanage , status = 1)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/accepted_donations.html',content)

@login_required
def AcceptedDonationsRecCan(request):
    if request.method == 'POST':
        val = int(request.POST["val"])
        id1 = request.POST["id1"]
        donatevaluables.objects.filter( tid = id1).update(status = val)
        k=donatevaluables.objects.get( tid = id1,status=2)
        Transport.objects.filter(danation_id=k.pk,status=1).update(status=3)
        if val == 2:
            messages.success(request,'Successfully received the donation')
            return redirect('orphanageadmin:o_accepteddonations')
        else:
            messages.warning(request,'Successfully cancelled the donation')
            return redirect('orphanageadmin:o_accepteddonations')

@login_required
def ReceivedDonations(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = donatevaluables.objects.filter(orphanage_id = orphanage , status = 2)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/received_donations.html',content)

@login_required
def MoneyDonations(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = donatemoney.objects.filter(orphanage_id = orphanage,status=1)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/moneydonations.html',content)


@login_required
def RequestedEvents(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = Events.objects.filter(orphanage_id = orphanage,status = 'Freshly Applied')
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/requestedevents.html',content)

@login_required
def AcceptedEvents_ChangeStatus(request):
    if request.method == 'POST':
        val = int(request.POST["val"])
        id1 = request.POST["id1"]
        if val == 1:
            Events.objects.filter( id = id1).update(status = 'Accepted')
            messages.success(request,'Successfully accepted the request')
            return redirect('orphanageadmin:o_requestedevents')
        else:
            Events.objects.filter( id = id1).update(status = 'Rejected')
            messages.warning(request,'Successfully rejected the request')
            return redirect('orphanageadmin:o_requestedevents')

@login_required
def AcceptedEvents(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    a=Events.objects.filter(orphanage_id = orphanage,status = 'Accepted')
    l=[]
    for i in a:
        print(i.date_of_event)
        q=[None]*5
        g,h,j=str(i.date_of_event).split('-')
        q[0]=int(g)
        q[1]=int(h)
        q[2]=int(j)
        q[3]=i.event
        q[4]=i.pk
        print(i.date_of_event)
        l.append(q)
    b=json.dumps(l)
    return render(request,'orphanageadmin/acceptedevents.html',context={'t':b})

def showevent(request,id):
    a=Events.objects.get(pk=id)
    return render(request,'orphanageadmin/showevent.html',context={'t':a,'b':1})

def deleteevent(request,id):
    a=Events.objects.get(pk=id)
    a.delete()
    messages.warning(request,'Successfully Deleted the event')
    return render(request,'orphanageadmin/showevent.html',context={'b':0})


@login_required
def JoinOrphan(request):
    user = request.user
    return render(request,'orphanageadmin/joinorphan.html')

@login_required
def Insertorphan(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
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
            return redirect('orphanageadmin:o_joinorphan')
        else:
            p = Orphan.objects.create(orphanage_id=orphanage,orphan_name=orphan_name,date_of_birth=date_of_birth,gender=gender,special_skills=special_skills)
            p.save()
            messages.success(request,'Added orphan successfully')
            return redirect('orphanageadmin:o_joinorphan')

@login_required
def OrphanDetails(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = Orphan.objects.filter(orphanage_id = orphanage)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/orphans.html',content)

@login_required
def OrphanDetailsDel(request):
    if request.method == 'POST':
        id1 = request.POST["id1"]
        Orphan.objects.filter(id = id1).delete()
    return redirect('orphanageadmin:o_orphandetails')


@login_required
def EmergencyRequest(request):
    user = request.user
    return render(request,'orphanageadmin/emergency_request.html')

def PostEmergencyRequest(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    if request.method == 'POST':
        problem = request.POST["problem"]
        requirement = request.POST["requirement"]
        p = Emergency(orphanage_id = orphanage, situation = problem , requirement = requirement,status=1)
        p.save()
        messages.success(request,'Successfully Posted')
        return redirect('orphanageadmin:o_emergencyrequest')

@login_required
def EmergencyCancel(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = Emergency.objects.filter(orphanage_id = orphanage,status = 1)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/emergencycancel.html',content)

@login_required
def EmergencyPostRemove(request):
    if request.method == 'POST':
        id1 = request.POST["id1"]
        Emergency.objects.filter(id = id1).update(status = 0)
        messages.success(request,'Post removed successfully')
        return redirect('orphanageadmin:o_emergencycancel')

@login_required
def HistoryOfPosts(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = Emergency.objects.filter(orphanage_id = orphanage,status = 1)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/historyofposts.html',content)

@login_required
def Requested_orphan(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = AddOrphan.objects.filter(orphanage_id = orphanage,ref_no = 0)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/requestedorphan.html',content)

@login_required
def AccReq_orphan(request):
    if request.method == 'POST':
        val = int(request.POST["val"])
        id1 = request.POST["id1"]
        print(val)
        AddOrphan.objects.filter(id = id1).update(ref_no = val)
        if val == 1:
            messages.success(request,'Successfully accepted the request')
            return redirect('orphanageadmin:o_requestedorphan')
        else:
            messages.warning(request,'Successfully rejected the request')
            return redirect('orphanageadmin:o_requestedorphan')

@login_required
def Accepted_orphan(request):
    user = request.user
    orphanage = Orphanage.objects.get(orphanage_id = user)
    donation_request = AddOrphan.objects.filter(orphanage_id = orphanage,ref_no = 1)
    content = {'donation_request':donation_request}
    return render(request,'orphanageadmin/acceptedorphan.html',content)
