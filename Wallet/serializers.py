from dataclasses import fields
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from Wallet.models import PersonalWallet, Transaction


class SetAccountFundingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        