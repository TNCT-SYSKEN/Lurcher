from django import forms
from .models import OfflineParty

class PageCreateForm(forms.ModelForm):
    class Meta:
        model = OfflineParty
        fields = ['title','at_time','capacity', 'recruitment_start','recruitment_end', 'comment']

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"