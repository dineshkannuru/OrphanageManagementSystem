from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='h_index'),
    path('contact us',views.index1,name='contact_us'),
    path('api', views.followview.as_view(), name='api'),
]
