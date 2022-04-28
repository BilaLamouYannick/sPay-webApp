from dataclasses import fields
import imp
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.widgets import PasswordInput, TextInput, EmailInput, FileInput, NumberInput, DateInput

from OAuth.models import User, PersonalAccount, EntrepriseAccount


class PersonalSignUpForm(UserCreationForm):
    # first_name = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'first_name'}))
    # last_name = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'last_name'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class':'form-control', 'placeholder':'', 'type':'date'}))
    personal_phone_number = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    personal_address = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')
        exclude = ('username', )
        widgets = {
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}),
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
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
    entreprise_phone_number = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    entreprise_address = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    entreprise_localisation = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    entreprise_description = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}))
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')
        exclude = ('username', )
        widgets = {
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}),
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':''}),
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
            entreprise_phone_number = self.cleaned_data.get("entreprise_phone_number"),
            entreprise_address = self.cleaned_data.get("entreprise_address"),
            entreprise_localisation = self.cleaned_data.get("entreprise_localisation"),
            entreprise_description = self.cleaned_data.get("entreprise_description")
        )
        return user