from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from registration.form import CustomAuthForm

app_name = 'registration'
urlpatterns = [
    path('', views.index, name='profile'),
    # path('donate_history', views.index1, name='donate_history'),
    # path('join_orphan', views.index2, name='join_orphan'),
    # path('near_you', views.index3, name='near_you'),
    # path('pending', views.index4, name='pending'),

    path('login', views.login_view, name='login'),
    path('register', views.signup, name='signup'),
    path(r'getData/<slug:user_type>/', views.get_data, name='get_data'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
         name='activate'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout/', views.logout_view, name= 'logout'),
    path('solution',views.solution,name='solution'),
    path('result',views.result,name='r_result1'),



    # path(r'password_reset/', auth_views.PasswordResetView.as_view() , name= 'password_reset'),
    # path(r'password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #
    # path(r'reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_engine='registration/password_reset_confirm.html'), name= 'password_reset_complete'),




    # path('register', views.orphanage_signup, name='orphanage_signup'),
    # path('login_result', views.loginstatus, name='loginstatus'),
    # path('login12', views.login12, name='login12'),
    # path('login1', views.login1, name='login1'),
    # path('signup1/user', views.user_signup1, name='user_signup1'),
    # path('signup12/user', views.user_signup12, name='user_signup12'),
    # path('signup1/orphanage', views.orphanage_signup1, name='orphanage_signup1'),
    # path('signup12/orphanage', views.orphanage_signup12, name='orphanage_signup12'),

]
