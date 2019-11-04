from django.shortcuts import render, redirect, reverse

from homepage.models import Orphanage, Type, UserDetails
from registration.form import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    return render(request, 'registration/profile.html')


def index1(request):
    return render(request, 'registration/donate-history.html')


def index2(request):
    return render(request, 'registration/join-orphan.html')


def index3(request):
    return render(request, 'registration/near-you.html')


def index4(request):
    return render(request, 'registration/pending.html')


def signup(request):
    if request.method == "POST":
        new_user_form = RegisterForm(request.POST)
        if new_user_form.is_valid():
            new_user = User.objects.create_user(
                username=new_user_form.cleaned_data["username"],
                password=new_user_form.cleaned_data["password"],
                email=new_user_form.cleaned_data["email"]
            )

            new_user.first_name = new_user_form.cleaned_data["first_name"]
            new_user.last_name = new_user_form.cleaned_data["last_name"]

            user_details = UserDetails.objects.create(
                user_id=new_user,
                date_of_birth=request.POST["DOB"],
                gender=request.POST["gender"],
                phone_no=request.POST["phone_number"]
            )
            user_type = Type.objects.create(
                user=new_user,
                ref_no=1
            )
            new_user.save()
            user_details.save()
            user_type.save()
            print("Form is valid")
            return HttpResponse("<h1>New user created successfully</h1>")
        else:
            print("Form Invalid")
            return render(request, 'registration/signup_page.html', {"signup_form": new_user_form})
    else:
        new_form = RegisterForm()
        print("Invalid request")
        return render(request, 'registration/signup_page.html', {"signup_form": new_form})


def loginstatus(request):
    return render(request, 'registration/login_success.html')


def login1(request):
    return render(request, 'registration/login.html')


def login12(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("User is " + request.user.username)
        print(user, username, password)
        if user is not None:
            login(request, user)
            type = Type.objects.get(user=user)
            if type.ref_no == 1:
                return redirect(reverse('userdashboard1:u_home', kwargs={'id1': user.id}))
        else:
            return render(request, 'registration/login.html')


# def login12_django_form(request):
#     if request.method == "POST":


def user_signup1(request):
    return render(request, 'registration/user_signup.html')


def user_signup12(request):
    if request.method == "POST":
        new_user = User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
            email=request.POST["email"],
        )
        user_details = UserDetails.objects.create(
            user_id=new_user,
            date_of_birth=request.POST["DOB"],
            gender=request.POST["gender"],
            phone_no=request.POST["phone_number"]
        )

        user_type = Type.objects.create(
            user=new_user,
            ref_no=1
        )
        new_user.save()
        user_details.save()
        user_type.save()
        return HttpResponse("<h1>New user created successfully</h1>")


def orphanage_signup1(request):
    return render(request, 'registration/orphanage_signup.html')


def orphanage_signup(request):
    try:
        print(request)
        type(request)
        if request.method == "POST":
            new_user_form = RegisterForm(request.POST)
            if new_user_form.is_valid():
                new_user = User.objects.create_user(
                    username=new_user_form.cleaned_data["username"],
                    password=new_user_form.cleaned_data["password"],
                    email=new_user_form.cleaned_data["email"]
                )
                new_orphanage_user = Orphanage.objects.create(
                    orphanage_name=request.POST["orphanage_name"],
                    year_of_establishment=request.POST["year_of_establishment"],
                    address=request.POST["address"],
                    phone_no=request.POST["phone_number"],
                    description=request.POST["description"],
                    image=request.FILES.get("orphanage_image"),
                    lat=request.POST["current_latitude"],
                    lon=request.POST["current_longitude"]
                )

                user_type = Type.objects.create(
                    user=new_user,
                    ref_no=2
                )
                new_user.save()
                new_orphanage_user.save()
                user_type.save()
                return HttpResponse("<h1>New orphanage user created successfully</h1>")
            else:
                print("Form Invalid")
                return render(request, 'registration/orphanage_signup.html', {"signup_form": new_user_form})
        else:
            new_form = RegisterForm()
            print("Invalid request")
            return render(request, 'registration/orphanage_signup.html', {"signup_form": new_form})
    except:
        return HttpResponse("Some unexpected error has occurred.")



def signup1(request):
    return render(request, 'registration/signup_page.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.path_info)
