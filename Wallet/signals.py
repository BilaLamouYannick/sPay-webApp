from urllib import response
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from Wallet.models import PersonalWallet, Transaction, Mtn_API_Account
from Wallet.api import MTN_WalletClient as MTN


@receiver(post_save, sender=Transaction)
def accountFunding(sender, instance, created, **kwargs):
    if instance.type_transaction == "AccountFunding":
        if created:
            transaction_amout = instance.amout
            uid_user_receiver = instance.receiver.uid
            
            
            if instance.operator == 'MTN':
                mtn_api = Mtn_API_Account.objects.get(api_user=instance.receiver, operator=instance.operator)
                mtn_api_user = mtn_api.api_user.uid
                mtn_api_key = mtn_api.api_key
                
                mtn = MTN(str(mtn_api_user))
                token = mtn.get_token(mtn_api_key)
                
                status_funding = mtn.set_account_funding(token['access_token'], transaction_amout, 2, 46733123453, "fais bien", "c'est top")
                
                info_funding = mtn.get_account_funding(token['access_token'])
                
                
                print(mtn_api_user)
                print(mtn_api_key)
                print(token['access_token'])
                
                
                if status_funding.status_code == 202:
                    receiver_personalWallet = PersonalWallet.objects.get(uid=uid_user_receiver)
                    receiver_personalWallet.balance = receiver_personalWallet.balance + transaction_amout
                    receiver_personalWallet.save(update_fields=['balance'])
                    instance.status = "SUCCESSFUL"
                    instance.save()
                
                elif status_funding.status_code == 409:
                    if info_funding['status'] == "FAILED":
                        instance.status = "FAILED"
                    elif info_funding['status'] == "PENDING":
                        instance.status = "PENDING"
                    instance.save()
                                    
            
    elif instance.type_transaction == "Transfert":
        if created:
            transaction_amout = instance.amout
            
            uid_user_sender = instance.sender.uid
            uid_user_receiver = instance.receiver.uid
            
            sender_personalWallet = PersonalWallet.objects.get(uid=uid_user_sender)
            receiver_personalWallet = PersonalWallet.objects.get(uid=uid_user_receiver)
            
            if sender_personalWallet.balance < transaction_amout:
                instance.status = "FAILED"
                instance.save()
            else:
                sender_personalWallet.balance = sender_personalWallet.balance - transaction_amout
                print(sender_personalWallet.balance)
                sender_personalWallet.save(update_fields=['balance'])
                
                receiver_personalWallet.balance = receiver_personalWallet.balance + transaction_amout
                receiver_personalWallet.save(update_fields=['balance'])
            
        
    elif instance.type_transaction == "Withdraw":
        if created:
            transaction_amout = instance.amout
            uid_user_sender = instance.sender.uid
            sender_personalWallet = PersonalWallet.objects.get(uid=uid_user_sender)
            
            if sender_personalWallet.balance < transaction_amout:
                instance.status = "FAILED"
                instance.save()
            else:
                sender_personalWallet.balance = sender_personalWallet.balance - transaction_amout
                sender_personalWallet.save(update_fields=['balance'])