
from django.urls import path
from . import views
app_name = 'userdashboard'

urlpatterns = [
    path('<int:id1>/donate_history', views.index1, name='donate_history'),
    path('<int:id1>/join_orphan', views.index2, name='join_orphan'),
    path('<int:id1>/near_you', views.index3, name='near_you'),
    path('<int:id1>/pending', views.index4, name='pending'),
    path('<int:id1>/donate_page', views.index5, name = 'donate_page'),
    path('<int:id1>/', views.home, name = 'u_home'),
    path('', views.auth_check, name= 'auth_check')

]