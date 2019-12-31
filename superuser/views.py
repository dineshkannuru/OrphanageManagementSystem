from django.shortcuts import render, HttpResponse,redirect
from homepage.models import Orphanage,Events,review,CateringCompany,catering,User
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

def viewreviews(request):
    h=request.POST.get('company')
    q=CateringCompany.objects.get(pk=int(h))
    a=review.objects.filter(company=q)
    
    return render(request, 'superuser/showreviews.html', {'allreviews':a})


@login_required
def viewcompanyprofile(request,pk):
    c=catering.objects.get(pk=pk)
    
    catering_company = CateringCompany.objects.get(company_name=c.company_name)
    return render(request, 'superuser/profile.html', {'user': catering_company.company_id, 'company': catering_company})


@login_required
def givereview(request):
    

    if request.method=='POST':
        print('jj')

        x=request.POST.get('name')
        print(x)
        q=catering.objects.get(event_id=int(x))
        w=CateringCompany.objects.get(company_name=q.company_name)
        description=request.POST.get('description')
        rating=request.POST.get('ratingnew')
        v=Events.objects.get(pk=int(x))
        v.canbereviewed='Completed'
        v.save()
        review.objects.create(description=description,rating=rating,user=request.user,company=w,date_created=datetime.datetime.now())
        messages.success(request, 'Added Review successfully')


        return render(request,'superuser/givereview.html')
    else:
        x=request.GET.get('name')
        print('x='+str(x))
        return render(request,'superuser/givereview.html',context={'x':x})




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
    now = datetime.datetime.now()
    c=Events.objects.filter(user_id=user,status = 'completed')
    b=Events.objects.filter(user_id=user,status = 'Accepted')
    a=b.union(c)
    print('len(a)=');print(len(a))
    for i in a:
        print(str(i.date_of_event))
        a,b,c=str(i.date_of_event).split('-')
        print('a='+str(a));
        print(b)
        print(c)
        print(now.year)
        print(now.month)
        print(now.day)
        eventdate=datetime.datetime(int(a),int(b),int(c))
        currentdate=datetime.datetime(now.year,now.month,now.day)
        if currentdate>eventdate and i.canbereviewed=='No':
            i.canbereviewed='Yes'
            i.save()
            print('yesssss')



    transport = catering.objects.filter(status=0)
    a = Events.objects.filter(user_id=user, status='Accepted')
    b = Events.objects.filter(user_id=user, status='Completed')
    print(type(a))

    a=a.union(b)
    transpose = []
    for accept in a:
        for trans in transport:
            if trans.event_id == accept.pk:
                accept.status = 10
                break



    context={'t':a,"transpose":transpose}

    return render(request,'superuser/acceptedevents.html',context)


#
# @login_required
# def acceptedevents(request):
#     user = request.user
#     a=Events.objects.filter(user_id=user,status = 'Accepted')
#     return render(request,'superuser/acceptedevents.html',context={'t':a})

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


#----------------------------------
def solution(request):
    user = request.user
    #print(user)
    id=request.POST['name']
    print(id,'###')
    data=catering.objects.filter(event_id=id)
    for each in data:
        h=each.event_id
        l=Events.objects.get(pk=h)
        #print(l.user_id,User.objects.get(username=user))
        if l.user_id==User.objects.get(username=user)  : #0 means not delivered
            print(l.pk)
            data1=catering.objects.filter(event_id=l.pk)
            print(data1)

            check = data1[0].items
            check = check.replace('[', '')
            check = check.replace(']', '')
            check = check.split(',')

            break;
    return render(request, 'superuser/accep.html', {"data1": data1, "check": check})

def result(request):
    if request.method == "POST":
        id = request.POST['name']
        print(id, '123')
        data = catering.objects.get(pk=id)
        k = data.event_id
        h = catering.objects.filter(event_id=k)
        # print(data.company_name)

        data.status = '1'  # 1 means Accepted
        data.save()
        l = Events.objects.get(pk=data.event_id)
        l.status = 'completed'  # 1 means Accepted
        l.save()
        for each in h:
            if str(each.pk) != str(id):
                print(each.event_id, id)
                each.status = '2'
                each.save()  # 2 means Rejected
        return redirect('superuser:acceptedevents')