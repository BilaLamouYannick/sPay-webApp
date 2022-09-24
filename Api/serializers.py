from dataclasses import fields
from pyexpat import model
from django.conf import settings
# AUTH_USER_MODEL

from OAuth.models import User

from django.contrib.auth import authenticate

from rest_framework import serializers

from Wallet.models import Wallet, Transaction
from django.contrib.auth import get_user_model
from Wallet.utils import OPERATOR, STATUS_TRANSACTIONS, TYPE_TRANSACTIONS

class LoginSerializer(serializers.Serializer):
    
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs
    
    
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
        

class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = "__all__"
        

class TransactiontSerialize(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = [
            'uid', 'sender', 'receiver', 'sender_number', 'receiver_number',
            'amount', 'status', 'type_transaction', 'operator'
        ]