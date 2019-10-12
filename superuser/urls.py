from django.contrib import admin
from django.urls import path,include
from superuser import views
from django.conf import settings
from django.conf.urls.static import static

app_name='superuser'
urlpatterns = [
    path('freshlyapplied/', views.freshlyapplied,name='freshlyapplied'),
    path('accepted/', views.accepted,name='accepted'),
    path('rejected/', views.rejected,name='rejected'),
    path('check/', views.check,name='check'),
    

]
