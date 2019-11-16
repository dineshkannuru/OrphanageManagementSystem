from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('' , views.index , name='h_index'),
    path('contact us',views.index1,name='contact_us'),
    #path('api', views.followview.as_view(), name='api'),
    #path('api11', views.followview1.as_view(), name='api11'),
    url(r'api11/(?P<company_name>[A-Z a-z 0-9]+)$', views.followview1.as_view(), name='api11'),
    url(r'api/(?P<company_name>[A-Z a-z 0-9]+)$', views.followview.as_view(), name='api'),
    url(r'token/(?P<company_name>[A-Z a-z]+)/(?P<password>[A-Z a-z 0-9]+)$',views.gettoken.as_view(),name='token'),
    url(r'api1/(?P<company_name>[A-Z a-z 0-9]+)$', views.transport.as_view(), name='api1'),
    url(r'api12/(?P<id>[0-9]+)/(?P<company_name>[A-Z a-z 0-9]+)$', views.transportid.as_view(), name='api12'),
    url(r'api123/(?P<company_name>[A-Z a-z 0-9]+)$', views.transport1.as_view(), name='api123'),
    url(r'api1234/(?P<company_name>[A-Z a-z 0-9]+)$', views.transport2.as_view(), name='api1234'),
    url(r'api12345/(?P<id>[0-9]+)/(?P<company_name>[A-Z a-z 0-9]+)$', views.transport3.as_view(), name='api12345'),
]
