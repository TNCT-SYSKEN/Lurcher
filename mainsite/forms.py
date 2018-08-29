from django import forms
from .models import OfflineParty

class DateInput(forms.DateInput):
    input_type = 'date'

class PageCreateForm(forms.ModelForm):
    class Meta:
        model = OfflineParty
        fields = ['title', 'capacity', 'recruitment_start','recruitment_end', 'comment']
        widgets = {
            'recruitment_start': DateInput(),
            'recruitment_end': DateInput()
        }

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"