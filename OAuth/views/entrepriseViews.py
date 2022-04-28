from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib import messages

from ..models import User
from ..forms import EntrepriseSignUpForm


class EntrepriseSignUpView(CreateView):
    model = User
    form_class = EntrepriseSignUpForm
    template_name = 'registration/signup_entreprise.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'entreprise'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        messages.success(self.request, 'Interests updated with success!')
        return redirect('/accounts/login/')
        # return super().form_valid(form)