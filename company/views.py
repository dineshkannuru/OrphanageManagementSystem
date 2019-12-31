from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from homepage.models import User, CateringCompany,review
from rest_framework.authtoken.models import Token


# Create your views here.
def ureviews(request):
    q=CateringCompany.objects.get(company_id=request.user)
    a=review.objects.filter(company=q)
    
    return render(request, 'company/showreviews.html', {'allreviews':a})

def profile(request):
    user = User.objects.get(username=request.user)
    catering_company = CateringCompany.objects.get(company_id=user)
    token=Token.objects.get(user=user)
    return render(request, 'company/profile.html', {'user': user, 'company': catering_company,'token':token})

@login_required
def profileupdate(request):
    user = request.user
    print(user)
    qs = User.objects.get(username=user)
    qs1=CateringCompany.objects.get(company_id=qs)
    #content = {'orphanage_name':orphanage.orphanage_name}
    #print(qs.first_name,qs.last_name,qs.email)
    return render(request,'company/edit_profile.html',{"qs":qs,"qs1":qs1})

@login_required
def editprofile(request):
    if request.method == 'POST':
        user = request.user
        print(user)
        empty=''
        company_name=request.POST.get('company_name')
        email=request.POST['email']
        address=request.POST['address']
        description=request.POST['description']
        #address=request.POST['address']
        qs = User.objects.get(username=user)
        qs1 = CateringCompany.objects.get(company_id=qs)
        if email==empty:
            pass
        else:
            qs.email=email


        if company_name ==empty:
            pass
        else:
            qs1.company_name=company_name
        if address ==empty:
            pass
        else:
            qs1.address=address
        if description==empty:
            pass
        else:
            qs1.description=description

        qs.save()
        qs1.save()
        user = User.objects.get(username=user)
        company = CateringCompany.objects.get(company_id=user)

        # content = {'orphanage_name':orphanage.orphanage_name}
        # print(qs.first_name,qs.last_name,qs.email)
        return render(request, 'company/profile.html', {"company": company, "user": user})


