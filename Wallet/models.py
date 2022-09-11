from django.db import models
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from OAuth.models import PersonalAccount, EntrepriseAccount, User

from Wallet.utils import TYPE_TRANSACTIONS, STATUS_TRANSACTIONS, OPERATOR
import uuid

# Create your models here.

class Wallet(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_number = models.CharField(max_length=250, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    balance = models.DecimalField(_("balance"), blank=True, default=0, max_digits=100, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
    
    
class Transaction(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # models.ManyToManyField("app.Model", verbose_name=_(""))
    # sender = models.ManyToManyField(PersonalWallet, related_name="sender", unique=False)
    # receiver = models.ManyToManyField(PersonalWallet, related_name="receiver", unique=False)
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="sender", null=True, blank=True, unique=False)
    receiver = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="receiver", null=True, blank=True, unique=False)
    sender_number = models.CharField(max_length=250, blank=True, null=True)
    receiver_number = models.CharField(max_length=250, blank=True, null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=250, choices=STATUS_TRANSACTIONS)
    created = models.DateTimeField(auto_now_add=True)
    type_transaction = models.CharField(max_length=250, choices=TYPE_TRANSACTIONS)
    operator = models.CharField(max_length=50, choices=OPERATOR)
    
    def __str__(self):
        return str(self.uid)
    
    
class Mtn_API_Account(models.Model):
    api_user = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=350)
    # api_key_disb = models.CharField(max_length=350)
    operator = models.CharField(max_length=50, choices=OPERATOR)
    
    class Meta:
        verbose_name = "Mtn API Account"
        verbose_name_plural = "Mtn API Accounts"
    
    def __str__(self):
        return str(self.api_user)