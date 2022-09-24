from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView


from ..models import User
from ..forms import PersonalSignUpForm

class PersonalSignUpView(CreateView):
    model = User
    form_class = PersonalSignUpForm
    template_name = 'registration/signup_personal.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'personal'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/accounts/login/')
        # return super().form_valid(form)

