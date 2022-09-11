from django.urls import path
from Dashboard.views import entrepriseViews, personalViews


urlpatterns = [
    path('dashbord/personnal/', personalViews.index, name='personal_wallet'),
    path('dashbord/personnal/withdraw', personalViews.withdraw, name='personal_withdraw'),   
    path('dashbord/personnal/accountFunding', personalViews.accountFunding, name='personal_accountFunding'),
    path('dashbord/personnal/transfert', personalViews.transfert, name='personal_transfert'),
    
    
    # Entrprise
    path('dashbord/entreprise/', entrepriseViews.index, name='entreprise_wallet'),
    path('dashbord/entreprise/withdraw', entrepriseViews.withdraw, name='entreprise_withdraw'),
]