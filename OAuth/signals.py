from django.db.models.signals import post_save
from django.dispatch import receiver

from OAuth.models import PersonalAccount
from Wallet.models import PersonalWallet, Mtn_API_Account
from Wallet.api import MTN_WalletClient


@receiver(post_save, sender=PersonalAccount)
def create_personal_wallet(sender, instance, created, **kwargs):
    if created:
        PersonalWallet.objects.create(personal=instance)
        
        
@receiver(post_save, sender=PersonalWallet)
def create_mtn_API_account(sender, instance, created, **kwargs):
    if created:
        
        # API creation user pour l'utilisateur
        uid_user = str(instance.uid)
        mtn = MTN_WalletClient(uid_user)
        api_usr = mtn.create_api_user()
        if api_usr.status_code == 201:
            apikey = mtn.get_api_key()
            Mtn_API_Account.objects.create(api_user=instance, api_key=apikey, operator="MTN")
            # new_API_Account = Mtn_API_Account.objects.create(api_user=instance, api_key=apikey, operator="MTN")
            
        
        