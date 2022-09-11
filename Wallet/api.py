from enum import unique
from urllib import response
from django.db import transaction
import requests, json, uuid, base64

from django.conf import settings

import http.client, urllib.request, urllib.parse, urllib.error, base64

# key_user = settings.COLLECTIONS_SUBSCRIPTION_KEY_USER_CREATE
# key_trans = settings.COLLECTIONS_SUBSCRIPTION_KEY_TRANS_CREATE


class MTN_WalletClient:

    # def __init__(self, unique_ref, subscription_key_user_create, subscription_key_trans_create):
    def __init__(self, unique_ref):
        self.url = "https://sandbox.momodeveloper.mtn.com"
        self.unique_ref = unique_ref
        # self.subscription_key_user_create = subscription_key_user_create
        # self.subscription_key_trans_create = subscription_key_trans_create
        self.collections_subscription_key_user_create = settings.COLLECTIONS_SUBSCRIPTION_KEY_USER_CREATE
        self.collections_subscription_key_trans_create = settings.COLLECTIONS_SUBSCRIPTION_KEY_TRANS_CREATE
        
        self.disbursements_subscription_key_user_create = settings.DISBURSEMENTS_SUBSCRIPTION_KEY_USER_CREATE
        self.disbursements_subscription_key_trans_create = settings.DISBURSEMENTS_SUBSCRIPTION_KEY_TRANS_CREATE

    
    def create_api_user(self):
        url = self.url + '/v1_0/apiuser'
        body = {
            "providerCallbackHost": "string"
        }
        headers = {
            'X-Reference-Id': self.unique_ref, 
            'Content-type': 'application/json', 
            'Ocp-Apim-Subscription-Key': self.collections_subscription_key_user_create
        }

        try:
            response = requests.post(url, data=json.dumps(body), headers=headers)
        except Exception as e:
            raise e

        return response
    
    
    def create_api_user_disb(self):
        url = self.url + '/v1_0/apiuser'
        body = {
            "providerCallbackHost": "string"
        }
        headers = {
            'X-Reference-Id': self.unique_ref, 
            'Content-type': 'application/json', 
            'Ocp-Apim-Subscription-Key': self.disbursements_subscription_key_user_create
        }

        try:
            response = requests.post(url, data=json.dumps(body), headers=headers)
        except Exception as e:
            raise e

        return response


    def get_api_key(self):
        url = self.url + f'/v1_0/apiuser/{self.unique_ref}/apikey'
        body = {
            "providerCallbackHost": "string"
        }
        headers = {
            'Ocp-Apim-Subscription-key': self.collections_subscription_key_user_create
        }

        try:
            response = requests.post(url, data=json.dumps(body), headers=headers).json()['apiKey']
        except Exception as e:
            raise e
        
        return response
    
    
    def get_api_key_disb(self):
        url = self.url + f'/v1_0/apiuser/{self.unique_ref}/apikey'
        body = {
            "providerCallbackHost": "string"
        }
        headers = {
            'Ocp-Apim-Subscription-key': self.disbursements_subscription_key_user_create
        }

        try:
            response = requests.post(url, data=json.dumps(body), headers=headers).json()['apiKey']
        except Exception as e:
            raise e
        
        return response


    def get_collection_token(self, apikey):
        url = self.url + f'/collection/token/'
        headers = {
            'Ocp-Apim-Subscription-key': self.collections_subscription_key_user_create
        }
        
        print(self.unique_ref, apikey, self.collections_subscription_key_user_create)

        try:
            response = requests.post(url, headers=headers, auth=(self.unique_ref, apikey)).json()
            
        except Exception as e:
            raise e

        print(response)
        return response
    
    
    def get_disbursement_token(self, apikey):
        url = self.url + f'/disbursement/token/'
        headers = {
            'Ocp-Apim-Subscription-key': self.disbursements_subscription_key_user_create
        }

        try:
            response = requests.post(url, headers=headers, auth=(self.unique_ref, apikey)).json()
        except Exception as e:
            raise e

        return response

    
    def set_account_funding(self, access_token, amount, externalId, partyId, payerMessage, payeeNote):
        """
            La fonction qui permet de faire l'approvisionnement du compte 
            MTN mobile money en utilisant le produit Collections
        """

        url = self.url + "/collection/v1_0/requesttopay"
        headers =   {
            "Authorization": 'Bearer ' + access_token, 
            # "X-Callback-Url": "",
            "X-Reference-Id": self.unique_ref,
            "X-Target-Environment": "sandbox",
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.collections_subscription_key_trans_create
        }

        body =   {
            "amount": amount,
            "currency": "EUR",
            "externalId": str(externalId),
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": str(partyId)
            },
            "payerMessage": str(payerMessage),
            "payeeNote": str(payeeNote)
        }

        try:
            response = requests.post(url, data=json.dumps(body).encode("ascii"), headers=headers)
        except Exception as e:
            raise e

        return response


    def get_account_funding(self, access_token):
        """
            La fonction qui permet de tester si la transaction a reussi
        """

        url = self.url + f'/collection/v1_0/requesttopay/{self.unique_ref}'
        headers =   {
            "Authorization": "Bearer " + access_token, 
            # "X-Callback-Url": "",
            "X-Reference-Id": self.unique_ref,
            "X-Target-Environment": "sandbox",
            "Ocp-Apim-Subscription-Key": self.collections_subscription_key_trans_create
        }
        
        try:
            response = requests.request("GET", url, headers=headers).json()
        except Exception as e:
            raise e
        
        return response
    

    
    def bc_autoriser(self, access_token):
        """
            La fonction qui permet de valider une trasaction pour le client
        """
        
        url = self.url + f'/collection/v1_0/bc-authorize'
        headers =   {
            "Authorization": "Bearer " + access_token, 
            # "X-Callback-Url": "",
            "X-Reference-Id": self.unique_ref,
            "X-Target-Environment": "sandbox",
            "Ocp-Apim-Subscription-Key": self.collections_subscription_key_trans_create
        }
        
        body =   {
            'login_hint': 'MSISDN',
            'scope': 2
        }
        
        try:
            response = requests.post(url, data=json.dumps(body).encode("ascii"), headers=headers)
        except Exception as e:
            raise e
        
        return response
    
    
    
    def set_account_withdraw(self, access_token, amount, externalId, partyId, payerMessage, payeeNote):
        """
            La fonction qui permet de retirer de l'argent
        """
        
        url = self.url + f'/disbursement/v1_0/transfer'
        headers =  {
            "Authorization": "Bearer " + access_token, 
            # "X-Callback-Url": "",
            "Content-Type": "application/json",
            "X-Reference-Id": self.unique_ref,
            "X-Target-Environment": "sandbox",
            "Ocp-Apim-Subscription-Key": self.disbursements_subscription_key_user_create
        }
        
        body =   {
            "payeeNote": payeeNote,
            "externalId": externalId,
            "amount": amount,
            "currency": "EUR",
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": partyId
            },
            "payerMessage": payerMessage
        }
        
        print(body)
        
        try:
            response = requests.post(url, data=json.dumps(body).encode("ascii"), headers=headers)
        except Exception as e:
            raise e

        return response
    
    
    def get_account_balance(self, access_token, amount, externalId, partyId, payerMessage, payeeNote):
        """
            La fonction qui permet d'avoir le solde du client
        """
        
        url = self.url + f'/collection/v1_0/account/balance'
        headers =  {
            "Authorization": "Bearer " + access_token, 
            # "X-Callback-Url": "",
            # "X-Reference-Id": self.unique_ref,
            "X-Target-Environment": "sandbox",
            "Ocp-Apim-Subscription-Key": self.collections_subscription_key_trans_create
        }
        pass
    
    
    def set_account_transfert(self, access_token, amount, externalId, partyId, payerMessage, payeeNote):
        """
            La fonction qui permet d'approvisionner un client
        """
        
        url = self.url + f'/remittance/v1_0/transfer'
        headers =  {
            "Authorization": "Bearer " + access_token, 
            # "X-Callback-Url": "",
            "X-Reference-Id": self.unique_ref,
            "X-Target-Environment": "sandbox",
            "Ocp-Apim-Subscription-Key": self.collections_subscription_key_trans_create
        }
        
        body =   {
            "payeeNote": payeeNote,
            "externalId": externalId,
            "amount": amount,
            "currency": "EUR",
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": partyId
            },
            "payerMessage": payerMessage
        }
        
        try:
            response = requests.post(url, data=json.dumps(body).encode("ascii"), headers=headers)
        except Exception as e:
            raise e

        return response

    
# p = MTN_WalletClient(str(uuid.uuid4()), 'd4e785ef01f944938f65aaff22c7cd82', 'ceb2573b0e134acaa52e958e80549a87')

# api_usr = p.create_api_user()

# if api_usr.status_code == 201:
#     print("Creation de User API effectif ,!")
#     apikey = p.get_api_key()
#     print("L'API Key a ete cree avec success!!: ", apikey)
#     print("Maintenant nous allons demander le Token ...")
#     token = p.get_token(apikey)
#     print(token['access_token'])
#     status_funding = p.set_account_funding(token['access_token'], 4000, 2, 46733123457, "fais bien", "c'est top")
#     print(status_funding)
#     print("La transaction s'est deroulee sans probleme. Merci")
#     info_funding = p.get_account_funding(token['access_token'])
#     # print(info_funding.status_code)
#     print(info_funding['status'])





