from django.contrib import admin

# Register your models here.

from Wallet.models import Wallet, Transaction, Mtn_API_Account

admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Mtn_API_Account)