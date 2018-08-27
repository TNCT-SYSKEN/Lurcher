from django.contrib import admin
from .models import Account, AccountCategory, OfflineParty

# Register your models here.
admin.site.register(Account)
admin.site.register(AccountCategory)
admin.site.register(OfflineParty)