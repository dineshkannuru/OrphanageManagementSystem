from django.urls import path
from . import views
app_name = 'orphanageadmin'

urlpatterns = [
    path('RequestedDonations/',views.RequestedDonations,name='o_requesteddonations'),
    path('AcceptedDonations/',views.AcceptedDonations,name='o_accepteddonations'),
    path('ReceivedDonations/',views.ReceivedDonations,name='o_receiveddonations'),
    path('EmergencyRequest/',views.EmergencyRequest,name='o_emergencyrequest'),
    path('EmergencyCancel/',views.EmergencyCancel,name='o_emergencycancel'),
    path('EmergencyPostRemove/',views.EmergencyPostRemove,name='o_emergencypostremove'),
    path('HistoryOfPosts/',views.HistoryOfPosts,name='o_historyofposts'),
    path('RequestedDonationsAccRej/',views.RequestedDonationsAccRej,name='o_accrej'),
    path('AcceptedDonationsRecCan/',views.AcceptedDonationsRecCan,name='o_reccan'),
    path('JoinOrphan/',views.JoinOrphan,name='o_joinorphan'),
    path('Insertorphan/',views.Insertorphan,name='o_insertorphan'),
    path('Profile/',views.Profile,name='o_profile'),
    path('result/',views.result,name='o_result'),
    path('result1',views.result1,name='o_result1'),
    path('MoneyDonations/',views.MoneyDonations,name='o_moneydonations'),
    path('OrphanDetails/',views.OrphanDetails,name='o_orphandetails'),
    path('RequestedEvents/',views.RequestedEvents,name='o_requestedevents'),
    path('AcceptedEvents/',views.AcceptedEvents,name='o_acceptedevents'),
    path('PostEmergencyRequest/',views.PostEmergencyRequest,name='o_postemergencyrequest'),
    path('AcceptedEvents_ChangeStatus/',views.AcceptedEvents_ChangeStatus,name='o_acceptedeventschangestatus'),
    path('PostEmergencyRequest/',views.PostEmergencyRequest,name='o_postemergencyrequest'),
    path('OrphanDetailsDel/',views.OrphanDetailsDel,name='o_orphandetailsdel'),
    path('showevent/<int:id>',views.showevent,name='showevent'),
    path('deleteevent/<int:id>',views.deleteevent,name='deleteevent'),
    path('Requested_orphan',views.Requested_orphan,name='o_requestedorphan'),
    path('AccReq_orphan',views.AccReq_orphan,name='o_accreqorphan'),
    path('Accepted_orphan',views.Accepted_orphan,name='o_acceptedorphan'),
]