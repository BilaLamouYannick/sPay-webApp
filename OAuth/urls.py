from django.urls import include, path

from OAuth.views import entrepriseViews, personalViews

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/personal/', personalViews.PersonalSignUpView.as_view(), name='personal_signup'),
    path('signup/entreprise/', entrepriseViews.EntrepriseSignUpView.as_view(), name='entreprise_signup'),
]