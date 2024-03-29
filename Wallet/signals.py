from urllib import response
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from Wallet.models import Wallet, Transaction, Mtn_API_Account
from Wallet.api import MTN_WalletClient as MTN


@receiver(post_save, sender=Transaction)
def accountFunding(sender, instance, created, **kwargs):
    if instance.type_transaction == "AccountFunding":
        if created:
            transaction_amount = instance.amount
            uid_user_receiver = instance.receiver.uid
            
            
            if instance.operator == 'MTN':
                mtn_api = Mtn_API_Account.objects.get(api_user=instance.receiver, operator=instance.operator)
                mtn_api_user = mtn_api.api_user.uid
                mtn_api_key = mtn_api.api_key
                
                mtn = MTN(str(mtn_api_user))
                token = mtn.get_collection_token(mtn_api_key)
                
                status_funding = mtn.set_account_funding(token['access_token'], int(transaction_amount), 2, 46733123453, "fais bien", "c'est top")
                
                info_funding = mtn.get_account_funding(token['access_token'])
                
                # print(mtn_api_user)
                # print(mtn_api_key)
                print(token['access_token'])
                
                print(status_funding)
                
                if status_funding.status_code == 202:
                    receiver_wallet = Wallet.objects.get(uid=uid_user_receiver)
                    receiver_wallet.balance = receiver_wallet.balance + int(transaction_amount)
                    receiver_wallet.save(update_fields=['balance'])
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
            transaction_amount = instance.amount
            
            uid_user_sender = instance.sender.uid
            uid_user_receiver = instance.receiver.uid
            
            sender_personalWallet = Wallet.objects.get(uid=uid_user_sender)
            receiver_personalWallet = Wallet.objects.get(uid=uid_user_receiver)
            
            if sender_personalWallet.balance < int(transaction_amount):
                instance.status = "FAILED"
                instance.save()
            else:
                sender_personalWallet.balance = sender_personalWallet.balance - int(transaction_amount)
                print(sender_personalWallet.balance)
                sender_personalWallet.save(update_fields=['balance'])
                
                receiver_personalWallet.balance = receiver_personalWallet.balance + int(transaction_amount)
                receiver_personalWallet.save(update_fields=['balance'])
                
                instance.status = "SUCCESSFUL"
                instance.save()
            
        
    # pour le retrait d'argent    
    elif instance.type_transaction == "Withdraw":
        if created:
            transaction_amount = instance.amount
            receiver_number = instance.receiver_number
            uid_user_sender = instance.sender.uid
            
            if instance.operator == 'MTN':
                
                mtn_api = Mtn_API_Account.objects.get(api_user=uid_user_sender, operator=instance.operator)
                mtn_api_user = mtn_api.api_user.uid
                mtn_api_key = mtn_api.api_key
                
                mtn = MTN(str(mtn_api_user))
                
                token = mtn.get_disbursement_token(mtn_api_key)
                
                print(token)
                status_funding = mtn.set_account_withdraw(token['access_token'], transaction_amount, 2, receiver_number, "fais bien", "c'est top")
            
                print(status_funding)
                sender_wallet = Wallet.objects.get(uid=uid_user_sender)
                
                
                if status_funding.status_code == 202:
                
                    if sender_wallet.balance < int(transaction_amount):
                        instance.status = "FAILED"
                        instance.save()
                    else:
                        sender_wallet.balance = sender_wallet.balance - int(transaction_amount)
                        instance.status = "SUCCESSFUL"
                        instance.save()
                        sender_wallet.save(update_fields=['balance'])
                
                elif status_funding.status_code == 409:
                    if info_funding['status'] == "FAILED":
                        instance.status = "FAILED"
                    elif info_funding['status'] == "PENDING":
                        instance.status = "PENDING"
                    instance.save()