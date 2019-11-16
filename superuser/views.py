from django.shortcuts import render, HttpResponse
from homepage.models import Orphanage,Events
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def requestedevents(request,pk=0):
    if request.method=='POST':
        print('hii')
        user = request.user
        a=Events.objects.get(pk=pk)
        a.status='Cancelled By User'
        a.save()
        messages.warning(request,'Event got cancelled')
        a=Events.objects.filter(orphanage_id = orphanage,status = 'Freshly Applied')
        return render(request,'superuser/requestedevents.html',context={'t':a})
    else:
        user = request.user
        a=Events.objects.filter(user_id=user,status = 'Freshly Applied')
        return render(request,'superuser/requestedevents.html',context={'t':a})
@login_required
def acceptedevents(request):
    user = request.user
    a=Events.objects.filter(user_id=user,status = 'Accepted')
    return render(request,'superuser/acceptedevents.html',context={'t':a})

@login_required
def rejectedevents(request):
    user = request.user
    a=Events.objects.filter(user_id=user,status = 'Rejected')
    return render(request,'superuser/rejectedevents.html',context={'t':a})


def freshlyapplied(request):
    orphanages = Orphanage.objects.filter(status='Freshly Applied')

    t_dict = {'t': orphanages}
    return render(request, 'superuser/basic.html', context=t_dict)


def accepted(request):
    orphanages = Orphanage.objects.filter(status='Accepted')

    t_dict = {'t': orphanages}
    return render(request, 'superuser/basic.html', context=t_dict)


def rejected(request):
    orphanages = Orphanage.objects.filter(status='Rejected')

    t_dict = {'t': orphanages}
    return render(request, 'superuser/basic.html', context=t_dict)


def check(request):
    print('atlssld')
    if request.method == 'POST':
        a = request.POST.get('orphanage_name')
        print(a)
        if 'ACCEPT' in request.POST:
            print('camehere')
            z = Orphanage.objects.get(orphanage_name=a)
            z.status = 'Accepted'
            z.save()
            orphanages = Orphanage.objects.filter(status='Accepted')
            t_dict = {'t': orphanages}
            return render(request, 'superuser/basic.html', context=t_dict)
        if 'REJECT' in request.POST:
            print('camehere2')
            z = Orphanage.objects.get(orphanage_name=a)
            z.status = 'Rejected'
            z.save()
            orphanages = Orphanage.objects.filter(status='Rejected')
            t_dict = {'t': orphanages}
            return render(request, 'superuser/basic.html', context=t_dict)
def addevent(request):
    if request.method=='POST':
        print('cametoaddevent')
        date=request.POST.get('date')


        orphanage=request.POST.get('orphanage')
        print('orphanage='+str(orphanage))
        print('date='+str(date))
        event=request.POST.get('event')
        print(event)
        description=request.POST.get('description')
        print(description)
        orp=Orphanage.objects.get(orphanage_name=orphanage)
        Events.objects.create(user_id=request.user,orphanage_id=orp,date_of_event=date,event=event,description=description)
        '''subject='Confirmation of event'
        message='Your event is confirmed'
        from_mail='sudarshan333u@gmail.com'
        to_list=[str(request.user.email)]
        send_mail(subject,message,from_mail,to_list,fail_silently=True)'''
        messages.success(request,'Added Event successfully')
        return render(request,'superuser/addevent.html',context={'f':1})

    else:
        a=Orphanage.objects.all()
        l=[]
        for i in a:
            l.append(i.orphanage_name)
        b=l[0]
        return render(request,'superuser/addevent.html',context={'t':l[1:],'b':b,'f':0})
def checkdate(request):
    print('ghjk')
    response_data={}
    response_data['is_success']=True
    orphanage=Orphanage.objects.get(orphanage_name=request.GET.get('orphanage'))
    date=request.GET.get('date')
    print('date='+str(date))
    print('orphanage='+str(orphanage))

    a=Events.objects.filter(orphanage_id=orphanage)
    flag=0
    print('highgh')
    if a:
        print('highghjkl')
        for i in a:
            print('wenthere')
            print(i.date_of_event)
            print(date)
            if str(i.date_of_event)==str(date):
                flag=1
    print('theend')
    if flag==1:
        print('validbefore')
        response_data['valid']=False
        print('validafter')
    else:
        response_data['valid']=True
    print('atlast')
    return JsonResponse(response_data)
