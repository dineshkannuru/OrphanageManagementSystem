from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def home(request, id1):
    user = request.user
    if request.user.is_authenticated:
        user = request.user
        print(user.email)
    else:
        print("Not authenticated")

    return HttpResponse("Hello " + user.username + ' your id is ' + str(user.id))