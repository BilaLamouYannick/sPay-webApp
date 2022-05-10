from dataclasses import fields
import imp
from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.widgets import PasswordInput, TextInput, EmailInput, FileInput, NumberInput, DateInput

from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

from OAuth.models import User, PersonalAccount, EntrepriseAccount

from django.forms.widgets import Widget

from django_countries.data import COUNTRIES


class PersonalSignUpForm(UserCreationForm):
    # first_name = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'first_name'}))
    # last_name = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'last_name'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class':'form-control', 'placeholder':'', 'type':'date'}))
    personal_phone_number = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    personal_address = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    
    # nationality = LazyTypedChoiceField(choices=countries, label='Nationality', required=False)
    
    class Meta(UserCreationForm.Meta):
        # use_required_attribute = False
        
        model = User
        fields = ('email', 'first_name', 'last_name', 'pays')
        exclude = ('username', )
        widgets = {
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}),
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'pays': CountrySelectWidget(attrs={'class':'form-control', 'placeholder':'', 'selected': 'CM'}),
            # 'pays': CountryField(blank_label='(select country)').formfield(required=False, Widget=CountrySelectWidget(attrs={'class':'form-control'})),
        }
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_personal = True
        user.save()
        PersonalAccount.objects.create(
            user=user,
            # first_name = self.cleaned_data.get("first_name"),
            # last_name = self.cleaned_data.get("last_name"),
            date_of_birth = self.cleaned_data.get("date_of_birth"),
            personal_phone_number = self.cleaned_data.get("personal_phone_number"),
            personal_address = self.cleaned_data.get("personal_address")
        )
        return user
    
    
    
class EntrepriseSignUpForm(UserCreationForm):
    entreprise_name = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    entreprise_phone_number = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    entreprise_address = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    entreprise_localisation = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    entreprise_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'style':"height: 50px;", 'placeholder':'', 'required':'required'}))
    
    entreprise_type = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    entreprise_branch_of_activity = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'pays')
        exclude = ('username', )
        widgets = {
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}),
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'pays': CountrySelectWidget(attrs={'class':'form-control', 'placeholder':'', 'initial':"{'country': 'CM'}"}),
        }
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_entreprise = True
        user.save()
        EntrepriseAccount.objects.create(
            user=user,
            # first_name = self.cleaned_data.get("first_name"),
            # last_name = self.cleaned_data.get("last_name"),
            entreprise_name = self.cleaned_data.get("entreprise_name"),
            entreprise_phone_number = self.cleaned_data.get("entreprise_phone_number"),
            entreprise_address = self.cleaned_data.get("entreprise_address"),
            entreprise_localisation = self.cleaned_data.get("entreprise_localisation"),
            entreprise_description = self.cleaned_data.get("entreprise_description"),
            entreprise_type = self.cleaned_data.get("entreprise_type"),
            entreprise_branch_of_activity = self.cleaned_data.get("entreprise_branch_of_activity")
        )
        return user