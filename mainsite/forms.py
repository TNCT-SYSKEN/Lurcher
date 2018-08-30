from django import forms
from .models import OfflineParty

class DateInput(forms.DateInput):
    input_type = 'date'

class PageCreateForm(forms.ModelForm):
    class Meta:
        model = OfflineParty
        fields = ['title', 'capacity', 'category', 'recruitment_start','recruitment_end', 'comment']
        widgets = {
            'recruitment_start': DateInput(),
            'recruitment_end': DateInput()
        }

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        attrs = {
            'data-live-search': 'true',
        }
        self.fields['category'].widget.attrs.update(attrs)
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['twitter_id', 'pref', 'category']
