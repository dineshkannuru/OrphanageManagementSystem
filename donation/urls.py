from django.urls import path, include
from donation import views
app_name = 'donation'

urlpatterns = [
    path('donate_money/',views.donatemoneyview,name='donatemoney'),
    path('donate_valuables/',views.donatevaluablesview,name='donate_valuables'),
    path('completed/',views.donation_completedview,name='completed'),
    path('paypal_home/<int:tid>/<int:amount>/<str:user_name>/<str:orphanage>/',views.paypal_home,name='inprogress'),
    path('paypal_return/',views.paypal_return),
    path('paypal_cancel/',views.paypal_cancel),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('facebook/',views.facebookview,name='facebook'),

]