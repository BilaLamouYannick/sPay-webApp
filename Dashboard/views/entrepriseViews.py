from distutils.command import clean
from django.shortcuts import render, redirect
from OAuth.models import EntrepriseAccount, User
from Wallet.models import Wallet, Transaction
from Dashboard.utils import get_number_card
from django.db.models import Q

from Wallet.forms import TransactionsForms


def index(request):
    account = User.objects.get(uid=request.user.uid)
    uid_wallet = Wallet.objects.get(user=account)
    str_uid_wallet = str(uid_wallet.uid)
    card_number = get_number_card(str_uid_wallet)
    
    transactions = Transaction.objects.filter(Q(receiver=str_uid_wallet) | Q(sender=str_uid_wallet))
    
    context = {
        'card_number': card_number,
        'transactions': transactions,
        'uid_wallet': uid_wallet,
    }
    return render(request, 'dashboard/entreprise/index.html', context)



def withdraw(request):
    account = User.objects.get(uid=request.user.uid)
    uid_wallet = Wallet.objects.get(user=account)
    str_uid_wallet = str(uid_wallet.uid)
    card_number = get_number_card(str_uid_wallet)
    
    form = TransactionsForms(initial={'type_transaction': 'Withdraw'})
    
    context = {
        'card_number': card_number,
        'uid_wallet': uid_wallet,
        'form': form,
    }
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        receiver_number = request.POST.get('receiver_number')
        operator = request.POST.get('operator')
        
        sender = uid_wallet
        
        type_transaction = request.POST.get('type_transaction')
        
        Transaction.objects.create(
            sender=sender,
            amount=amount,
            receiver_number=receiver_number,
            operator=operator,
            type_transaction=type_transaction
        )
        
        return redirect('entreprise_wallet')
    
    return render(request, 'dashboard/entreprise/withdraw.html', context)