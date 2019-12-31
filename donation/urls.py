from django.urls import path, include
from donation import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('money',views.testdonatemoney)
router.register('user', views.CurrentUserViewSet)
router.register('orphanage',views.testorphanage)


app_name = 'donation'

urlpatterns = [
    path('test/',include(router.urls)),
    path('api/',views.rest_moneyview,name='rest'),
    path('donate_money/',views.donatemoneyview,name='donatemoney'),
    path('emer_donate_money/<int:eid>/',views.emergencydonatemoneyview,name='emergencydonatemoney'),
    path('donate_valuables/',views.donatevaluablesview,name='donate_valuables'),
    path('donation_done/',views.donation_completedview,name='completed'),
    path('donation_interrupt/',views.donation_interruptview,name='cancel'),
    path('requestplaced/',views.donation_completedview,name='request_placed'),
    path('paypal_home/<int:tid>/<int:amount>/<str:orphanage_id1>/',views.paypal_home,name='inprogress'),
    path('paypal_return/',views.paypal_return),
    path('paypal_cancel/',views.paypal_cancel),
#    path('facebook/',views.facebookview,name='facebook'),
    path('social/',views.socialview,name='social'),
    path('Accepted/',views.acceptedview,name='accepted'),
    path('Rejected/',views.rejectedview,name='rejected'),
    path('history/',views.historyview,name='history'),
    path('received/',views.receivedview,name='received'),
    path('progress/',views.progressview,name='progress'),

]
