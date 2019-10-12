from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='o_home'),
    path('add_orphan/',views.addorphan,name='add_orphan'),
    path('insert_orphan/',views.insertorphan,name='insert_orphan'),
]