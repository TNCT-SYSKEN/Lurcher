from django.shortcuts import render
from .models import OfflineParty
from .forms import AddSettingsForm

# Create your views here.

def add_settings(request, party_id) :
    party = OfflineParty.objects.get(id = party_id)
    form = AddSettingsForm(request.POST or None, instance = party)

    if request.method == 'POST' and form.is_valid() :
        form.save()

    context = {
        'form': form
    }
    return render(request, 'mainsite/add-settings.html', context)
