from django.contrib import admin
from .models import Account, OfflineParty

# Register your models here.
admin.site.register(Account)
admin.site.register(OfflineParty)