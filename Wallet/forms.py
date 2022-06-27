from dataclasses import field
from django import forms
from Wallet.models import Transaction
from Wallet.utils import TYPE_TRANSACTIONS
from django.forms.widgets import PasswordInput

class TransactionsForms(forms.ModelForm):
    # type_transaction = forms.CharField(required=False)
    # type_transaction = forms.TypedChoiceField(
    #     choices=TYPE_TRANSACTIONS
    # )
    
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    class Meta:
        model = Transaction
        fields = [
            'sender', 'receiver', 'sender_number', 'receiver_number',
            'amount', 'status', 'type_transaction', 'operator'
        ]