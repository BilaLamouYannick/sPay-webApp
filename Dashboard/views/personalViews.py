import email
from django.dispatch import receiver
from django.shortcuts import render, redirect
from OAuth.models import User
from django.db.models import Q
from Wallet.models import Wallet, Transaction
from Dashboard.utils import get_number_card

from django.contrib.auth import authenticate

from Wallet.forms import TransactionsForms


def index(request):
    account = User.objects.get(uid=request.user.uid)
    uid_wallet = Wallet.objects.get(user=account)
    str_uid_wallet = str(uid_wallet.uid)
    
    card_number = Wallet.objects.get(user=account).cart_number
    
    transactions = Transaction.objects.filter(Q(receiver=str_uid_wallet) | Q(sender=str_uid_wallet))
    
    context = {
        'card_number': card_number,
        'transactions': transactions,
        'uid_wallet': uid_wallet,
    }
    return render(request, 'dashboard/personal/index.html', context)



def accountFunding(request):
    account = User.objects.get(uid=request.user.uid)
    uid_wallet = Wallet.objects.get(user=account)
    str_uid_wallet = str(uid_wallet.uid)
    card_number = Wallet.objects.get(user=account).cart_number
    
    form = TransactionsForms(initial={'type_transaction': 'AccountFunding'})
    
    context = {
        'card_number': card_number,
        'form': form,
        'uid_wallet': uid_wallet,
    }
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        sender_number = request.POST.get('receiver_number')
        operator = request.POST.get('operator')
        receiver = uid_wallet
        type_transaction = request.POST.get('type_transaction')
        # password = request.POST.get('password')
        # user = authenticate(request, email=request.user.email, password=password)
        
        if receiver is not None:
            Transaction.objects.create(
                receiver=receiver,
                amount=amount,
                sender_number=sender_number,
                operator=operator,
                type_transaction=type_transaction
            )
            return redirect('personal_wallet')
    
    return render(request, 'dashboard/personal/accounFunding.html', context)



def withdraw(request):
    account = User.objects.get(uid=request.user.uid)
    uid_wallet = Wallet.objects.get(user=account)
    str_uid_wallet = str(uid_wallet.uid)
    card_number = Wallet.objects.get(user=account).cart_number
    
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
        password = request.POST.get('password')
        user = authenticate(request, email=request.user.email, password=password)
        
        if user is not None:
            Transaction.objects.create(
                sender=sender,
                amount=amount,
                receiver_number=receiver_number,
                operator=operator,
                type_transaction=type_transaction
            )
            return redirect('personal_wallet')
    
    return render(request, 'dashboard/personal/withdraw.html', context)


def transfert(request):
    account = User.objects.get(uid=request.user.uid)
    uid_wallet = Wallet.objects.get(user=account)
    str_uid_wallet = str(uid_wallet.uid)
    card_number = Wallet.objects.get(user=account).cart_number
    
    form = TransactionsForms(initial={'type_transaction': 'Transfert'})
    
    context = {
        'card_number': card_number,
        'uid_wallet': uid_wallet,
        'form': form,
    }
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        cart_number = request.POST.get('receiver_number')
        
        
        # operator = request.POST.get('operator')
        
        operator = ('SPAY Account', 'SPAY Account')[0]
        
        sender = uid_wallet
        type_transaction = request.POST.get('type_transaction')
        password = request.POST.get('password')
        
        print(amount, cart_number)
        
        receiver = Wallet.objects.get(cart_number=str(cart_number))
        
        user = authenticate(request, email=request.user.email, password=password)
        
        if user is not None:
            Transaction.objects.create(
                sender=sender,
                amount=amount,
                receiver=receiver,
                operator=operator,
                type_transaction=type_transaction
            )
            return redirect('personal_wallet')
    
    return render(request, 'dashboard/personal/transfert.html', context)