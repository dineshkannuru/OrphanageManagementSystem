
from django.urls import path
from . import views
app_name = 'userdashboard'

urlpatterns = [
path('Profile',views.Profile,name='u_Profile'),
path('result1',views.profileupdate,name='u_result11'),
path('result12', views.editprofile, name='u_result12'),
]