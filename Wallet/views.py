from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from Wallet.serializers import SetAccountFundingSerializers
from Wallet.models import Transaction, PersonalWallet

from Wallet.api import MTN_WalletClient
# Create your views here.


# @api_view(['GET', 'POST'])
# def accountFunding(request):
#     type_transaction = 'AccountFunding'
#     if request.method == 'POST':
#         amount = request.get('amount', '')
#         phone_number = request.get('phone_number', '')
#         print(amount, phone_number)
#     else:    
#         context = {
#             'user': 'request',
#         }
#         return Response(context)

class SetAccountFunding(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = SetAccountFundingSerializers
    permission_class = (IsAuthenticated, )