
from django.urls import path
from . import views
app_name = 'userdashboard'

urlpatterns = [
path('Profile',views.Profile,name='u_Profile'),
path('result1',views.profileupdate,name='u_result11'),
path('result12', views.editprofile, name='u_result12'),
path('requestJoinOrphan', views.requestJoinOrphan, name = "request_joinorphan"),
path('acceptedJoinOrphanReqs', views.acceptedJoinOrphan_requests, name= "accepted_joinorphan"),
path('rejectedJoinOrphanReqs', views.rejectedJoinOrphan_requests, name= "rejected_joinorphan"),
path('pendingJoinOrphanReqs', views.pendingJoinOrphan_requests, name= "pending_joinorphan"),
path('about',views.about,name='u_aboutor'),
path('about1',views.about1,name='u_aboutor1'),
path('about_page',views.about_page,name='u_about_page'),
path('location',views.location,name='u_location'),
]
