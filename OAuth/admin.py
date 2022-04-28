from django.contrib import admin

from OAuth.models import User, PersonalAccount, EntrepriseAccount
# Register your models here.

admin.site.register(User)
admin.site.register(PersonalAccount)
admin.site.register(EntrepriseAccount)