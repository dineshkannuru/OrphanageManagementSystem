from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def index1(request, id1):
    return render(request, 'userdashboard/donate-history.html')


def index2(request):
    return render(request, 'userdashboard/join-orphan.html')


def index3(request):
    return render(request, 'userdashboard/near-you.html')


def index4(request):
    return render(request, 'userdashboard/pending.html')

def index5(request, id1):
    return render(request, 'userdashboard/donate_page.html')

def home(request, id1):
    user = request.user
    if request.user.is_authenticated:
        user = request.user
        print(user.email)
        return render(request, 'userdashboard/userdashboard.html')
    else:
        print("Not authenticated")


def auth_check(request):
    user = request.user
    if request.user.is_authenticated:
        user = request.user
        print(user.email)
    else:
        print("Not authenticated")

    return HttpResponse("Hello " + user.username + ' your id is ' + str(user.id))
