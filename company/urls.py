from django.urls import path
from . import views
app_name = 'company'

urlpatterns = [
    path('profile/', views.profile, name='c_profile'),
    path('result1',views.profileupdate,name='u_result11'),
    path('result12', views.editprofile, name='u_result12'),
    path('ureviews', views.ureviews, name='ureviews'),
]