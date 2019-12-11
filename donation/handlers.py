from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received,invalid_ipn_received
from django.views.decorators.csrf import csrf_exempt

def show_me_the_money(sender, **kwargs):
    print('test')
    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
     
        if ipn_obj.receiver_email != "paypalemail@gmail.com":
            # Not a valid payment
            return

        if ipn_obj.mc_gross == ipn_obj.amount and ipn_obj.mc_currency == 'USD':
            pk = ipn_obj.invoice
            dsr = DatasetRequest.objects.get(pk=pk)
            dsr.is_paid = True
            dsr.save()
    else:
        pass

print("FC barcelona")
valid_ipn_received.connect(show_me_the_money)
invalid_ipn_received.connect(show_me_the_money)

