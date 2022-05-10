from django.shortcuts import render
from OAuth.models import User
from django.db.models import Q
from Wallet.models import Wallet, Transaction
from Dashboard.utils import get_number_card


def index(request):
    account = User.objects.get(uid=request.user.uid)
    uid_wallet = Wallet.objects.get(user=account)
    str_uid_wallet = str(uid_wallet.uid)
    card_number = get_number_card(str_uid_wallet)
    
    transactions = Transaction.objects.filter(Q(receiver=str_uid_wallet) | Q(sender=str_uid_wallet))
    
    print(type(request.user.email), type(transactions[0].sender))
    context = {
        'card_number': card_number,
        'transactions': transactions,
        'uid_wallet': uid_wallet,
    }
    return render(request, 'dashboard/personal/index.html', context)