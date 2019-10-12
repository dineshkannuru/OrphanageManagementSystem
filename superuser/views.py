from django.shortcuts import render, HttpResponse
from homepage.models import Orphanage


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
