
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
path('pendingJoinOrphanReqs', views.pendingJoinOrphan_requests, name= "pending_joinorphan")
]
