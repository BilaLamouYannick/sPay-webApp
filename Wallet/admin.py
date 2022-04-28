from django.contrib import admin

# Register your models here.

from Wallet.models import PersonalWallet, Transaction, Mtn_API_Account

admin.site.register(PersonalWallet)
admin.site.register(Transaction)
admin.site.register(Mtn_API_Account)