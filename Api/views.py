from multiprocessing import context
from rest_framework import permissions, generics, views, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from django.contrib.auth import authenticate, login

from . import serializers

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from OAuth.models import PersonalAccount, EntrepriseAccount
from Wallet.models import Wallet, Transaction

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework.decorators import api_view

import uuid

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    
    # permission_classes = []
    permission_classes = [AllowAny,]

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        
        login(request, user)
        
        account = PersonalAccount.objects.get(user=user)
        
        wallet = Wallet.objects.get(user=user)
        
        str_uid_wallet = str(wallet.uid)
        
        transactions = Transaction.objects.filter(Q(receiver=str_uid_wallet) | Q(sender=str_uid_wallet))
        
        trans_obj = []
        
        fields = [
            'uid', 'sender', 'receiver', 'sender_number', 'receiver_number',
            'amount', 'status', 'type_transaction', 'operator'
        ]
        
        for elt in transactions:
            print(type(elt.uid))
            trans = {
                "uid": elt.uid,
                "sender": str(elt.sender),
                "receiver": str(elt.receiver),
                "sender_number": str(elt.sender_number),
                "receiver_number": str(elt.receiver_number),
                "amount": str(elt.amount),
                "status": str(elt.status),
                "type_transaction": str(elt.type_transaction),
                "operator": str(elt.operator)
            }
            trans_obj.append(trans)
        
        return Response({
            "user": serializers.UserSerializer(user, context={}).data,
            "transactions": trans_obj,
            "wallet": {"uid": wallet.uid, "cart_number": str(wallet.cart_number), "balance": wallet.balance, "user": str(wallet.user)}
        }, status=status.HTTP_200_OK)
    
    
class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
    

@api_view(['GET', 'POST'])
def accountFunding(request):
    if request.method == 'POST':
        # print(request.data['email'])
        
        print("yess")
        print(request.data)
        
        amount = request.data['amount']
        sender_number = request.data['sender_number']
        operator = request.data['operator']
        cart_number = request.data['cart_number']
        type_transaction = "AccountFunding"
        
        # print(uuid.UUID(receiver))
        
        wallet = Wallet.objects.get(cart_number=cart_number)
        print(wallet.uid)
        
        if cart_number is not None:
            Transaction.objects.create(
                receiver=wallet,
                amount=int(amount),
                sender_number=int(sender_number),
                operator=operator,
                type_transaction=type_transaction
            )
        
        return Response({"message": "Got some data!", "data": request.data}, status=status.HTTP_200_OK)
    return Response({"message": "AccountFunding!"})


@api_view(['GET', 'POST'])
def transfert(request):
    if request.method == 'POST':
        # print(request.data['email'])
        
        
        amount = request.data['amount']
        sender_number = request.data['sender_number']
        operator = request.data['operator']
        receiver_cart_number = request.data['receiver_cart_number']
        cart_number = request.data['cart_number']
        email = request.data['email']
        password = request.data['password']
        type_transaction = "Transfert"
        operator = ('SPAY Account', 'SPAY Account')[0]
        
        # print(uuid.UUID(receiver))
        
        wallet = Wallet.objects.get(cart_number=cart_number)
        receiver_wallet = Wallet.objects.get(cart_number=receiver_cart_number)
        
        user = authenticate(request, email=request.user.email, password=password)
        
        if cart_number is not None:
            Transaction.objects.create(
                receiver=wallet,
                amount=int(amount),
                sender_number=int(sender_number),
                operator=operator,
                type_transaction=type_transaction
            )
        
        return Response({"message": "Got some data!", "data": request.data}, status=status.HTTP_200_OK)
    return Response({"message": "AccountFunding!"})

# class TransactionsView(views.APIView):
#     def post(self, )

    
# {
#     "email": "alice@gmail.com",
#     "password": "audique10"
# }

# {
#     "amount": "1990",
#     "operator": "MTN",
#     "sender_number": "38740029877",
#     "cart_number":"4893 6646 5751 9946 8338"
# }