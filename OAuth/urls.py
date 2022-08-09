from django.urls import include, path

from OAuth.views import entrepriseViews, personalViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/personal/', personalViews.PersonalSignUpView.as_view(), name='personal_signup'),
    path('signup/entreprise/', entrepriseViews.EntrepriseSignUpView.as_view(), name='entreprise_signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]