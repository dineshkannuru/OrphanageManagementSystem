from paypal.standard.models import ST_PP_COMPLETED
from homepage.models import donatemoney
from paypal.standard.ipn.signals import valid_ipn_received,invalid_ipn_received
from django.views.decorators.csrf import csrf_exempt

def show_me_the_money(sender, **kwargs):
    print('test')
    ipn_obj = sender
    ipn_obj.mc_gross=int(ipn_obj.mc_gross)
    data=donatemoney.objects.filter(pk=ipn_obj.invoice)
    print(data[0].amount)
    if ipn_obj.payment_status == ST_PP_COMPLETED: 
        if ipn_obj.receiver_email == "sb-th3743389074@business.example.com":
            if ipn_obj.mc_gross == data[0].amount and ipn_obj.mc_currency == 'USD':
                data.update(paypal_transaction = ipn_obj.txn_id,status=2)
                print('Success')
                #pk = ipn_obj.invoice
                #dsr = DatasetRequest.objects.get(pk=pk)
                #dsr.is_paid = True
                #dsr.save()
                return
            else:                
                print("Error")
                data.update(status=1)

        else:
            print("Error")
            data.update(status=1)

print("FC barcelona")
valid_ipn_received.connect(show_me_the_money)


