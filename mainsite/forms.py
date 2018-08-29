from django import forms
from .models import OfflineParty

class PageCreateForm(forms.ModelForm):
    class Meta:
        model = OfflineParty
        fields = ['title','at_time','capacity','location_lat',
        'location_lng','recruitment_start','recruitment_end',
        'comment']
