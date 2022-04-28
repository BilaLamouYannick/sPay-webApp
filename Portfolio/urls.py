from django.urls import path
from Portfolio.views import home

urlpatterns = [
    path('', home, name='home'),
]