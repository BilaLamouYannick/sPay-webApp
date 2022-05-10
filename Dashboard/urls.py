from django.urls import path
from Dashboard.views import entrepriseViews, personalViews


urlpatterns = [
    path('dashbord/personnal/', personalViews.index, name='personal_wallet'),
    
    
    # Entrprise
    path('dashbord/entreprise/', entrepriseViews.index, name='entreprise_wallet'),
    path('dashbord/entreprise/withdraw', entrepriseViews.withdraw, name='entreprise_withdraw'),
]