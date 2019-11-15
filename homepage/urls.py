from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('' , views.index , name='h_index'),
    path('contact us',views.index1,name='contact_us'),
    path('api', views.followview.as_view(), name='api'),
    path('api11', views.followview1.as_view(), name='api11'),
    path('api1', views.transport.as_view(), name='api1'),
    url(r'api12/(?P<id>[0-9]+)$', views.transportid.as_view(), name='api12'),
    path('api123', views.transport1.as_view(), name='api123'),
    url(r'api1234/(?P<company_name>[A-Z a-z]+)$', views.transport2.as_view(), name='api1234'),

]
