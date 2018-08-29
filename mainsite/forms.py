from django import forms
from .models import OfflineParty

class AddSettingsForm(forms.ModelForm):
    class Meta:
        model = OfflineParty
        fields = ['location_lat', 'location_lng', 'at_time']