from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django_countries.fields import CountryField
from requests import request
# Create your models here.

from .manager import CustomUserManager
import uuid


class User(AbstractUser):
    
    username = None
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254, blank=False, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    pays = CountryField()
    verified = models.BooleanField(default=False)
    is_personal = models.BooleanField(default=False)
    is_entreprise = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    
class PersonalAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    personal_phone_number = models.CharField(max_length=50, blank=True)
    personal_address = models.CharField(max_length=250, blank=True)
    
    
    class Meta:
        verbose_name = "Personnal Account"
        verbose_name_plural = "Personnal Accounts"
    
    def __str__(self):
        return str(self.user.email)
    
    

class EntrepriseAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    entreprise_name = models.CharField(max_length=250, blank=True)
    entreprise_phone_number = models.CharField(max_length=250, blank=True)
    entreprise_address = models.CharField(max_length=250, blank=True)
    entreprise_localisation = models.CharField(max_length=250, blank=True)
    entreprise_description = models.TextField()
    entreprise_type = models.CharField(max_length=250, blank=True)
    entreprise_branch_of_activity = models.CharField(max_length=250, blank=True) 
    
    
    class Meta:
        verbose_name = "Entreprise Account"
        verbose_name_plural = "Entreprise Accounts"
    
    def __str__(self):
        return str(self.entreprise_name)