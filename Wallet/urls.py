from django.urls import path
from Wallet.views import SetAccountFunding

from rest_framework import routers


router = routers.DefaultRouter()
router.register('personal/transactions', SetAccountFunding)

urlpatterns = [
    # path('test/', accountFunding, name='accountFunding'), SetAccountFunding
    # path('test/', SetAccountFunding.as_view(), name='SetAccountFunding'),
]