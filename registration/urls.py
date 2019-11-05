from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from registration.form import CustomAuthForm

urlpatterns = [
    path('' , views.index , name='profile'),
    path('donate_history',views.index1,name='donate_history'),
    path('join_orphan' , views.index2 , name='join_orphan'),
    path('near_you' , views.index3 , name='near_you'),
    path('pending' , views.index4 , name='pending'),

    path('login', auth_views.LoginView.as_view(template_name="registration/login.html" ,  authentication_form=CustomAuthForm)),
    path('register', views.signup, name='signup'),
    path(r'getData/<slug:user_type>/', views.get_data, name='get_data'),
    # path('register', views.orphanage_signup, name='orphanage_signup'),
    # path('login_result', views.loginstatus, name='loginstatus'),
    # path('login12', views.login12, name='login12'),
    # path('login1', views.login1, name='login1'),
    # path('signup1/user', views.user_signup1, name='user_signup1'),
    # path('signup12/user', views.user_signup12, name='user_signup12'),
    # path('signup1/orphanage', views.orphanage_signup1, name='orphanage_signup1'),
    #path('signup12/orphanage', views.orphanage_signup12, name='orphanage_signup12'),


]



