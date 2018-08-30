from django import forms
from .models import Account, OfflineParty

class AddSettingsForm(forms.ModelForm):
    class Meta:
        model = OfflineParty
        fields = ['location_lat', 'location_lng', 'at_time']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['twitter_id', 'pref', 'category', 'access_token', 'access_token_secret']

class PageCreateForm(forms.ModelForm):
    class Meta:
        model = OfflineParty
        fields = ['title','at_time','capacity','location_lat',
        'location_lng','category','recruitment_start','recruitment_end',
        'comment']
