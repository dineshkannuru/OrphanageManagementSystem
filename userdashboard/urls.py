
from django.urls import path
from . import views
app_name = 'userdashboard1'

urlpatterns = [
    path('<int:id1>/', views.home, name = 'u_home'),

]