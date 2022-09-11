from django.db.models.signals import post_save
from django.dispatch import receiver

from OAuth.models import User, PersonalAccount, EntrepriseAccount
from Wallet.models import Wallet, Mtn_API_Account
from Wallet.api import MTN_WalletClient


def get_number_card(uid_wallet):
    card_number = list()
    card = list()
    number = ''.join(ch for ch in uid_wallet if ch.isnumeric())
    i = 0
    for el in number:
        card.append(el)
        i += 1
        if len(card) == 4:
            text = "".join(card)
            card = list()
            card_number.append(text)        
    
    card_number = " ".join(card_number)
    return card_number


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        
        Wallet.objects.create(user=instance)
        
        
        
@receiver(post_save, sender=Wallet)
def create_mtn_API_account(sender, instance, created, **kwargs):
    if created:
        
        # API creation user pour l'utilisateur
        uid_user = str(instance.uid)
        
        wallet = sender.objects.get(uid=instance.uid)
        wallet_uid = wallet.uid
        card_number = get_number_card(str(wallet_uid))
        
        wallet.cart_number = str(card_number)
        
        wallet.save()
        
        mtn = MTN_WalletClient(uid_user)
        api_usr = mtn.create_api_user()
        if api_usr.status_code == 201:
            apikey = mtn.get_api_key()
            Mtn_API_Account.objects.create(api_user=instance, api_key=apikey, operator="MTN")
            # new_API_Account = Mtn_API_Account.objects.create(api_user=instance, api_key=apikey, operator="MTN")
            

 
# Entreprise
        
# @receiver(post_save, sender=EntrepriseAccount)
# def create_entreprise_wallet(sender, instance, created, **kwargs):
#     if created:
#         EntrepriseWallet.objects.create(entreprise=instance)
        
        
# @receiver(post_save, sender=EntrepriseWallet)
# def create_mtn_API_account_entreprise(sender, instance, created, **kwargs):
#     if created:
        
#         # API creation user pour l'entreprise
#         uid_user = str(instance.uid)
#         mtn = MTN_WalletClient(uid_user)
#         api_usr = mtn.create_api_user()
#         if api_usr.status_code == 201:
#             apikey = mtn.get_api_key()
#             print("apikey", apikey)
#             Mtn_API_Account.objects.create(api_user=instance, api_key=apikey, operator="MTN")