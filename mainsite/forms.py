from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['twitter_id', 'pref', 'category', 'access_token', 'access_token_secret']
