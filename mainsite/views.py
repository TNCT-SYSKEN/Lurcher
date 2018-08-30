from django.shortcuts import render
from django.contrib import messages
from .models import OfflineParty
from .forms import AddSettingsForm

# Create your views here.

def add_settings(request, party_id) :
    party = OfflineParty.objects.get(id = party_id)
    form = AddSettingsForm(request.POST or None, instance = party)
    context = {
        'form': form
    }

    if form.is_valid() :
        context['location_undefined'] = not(form.cleaned_data['location_lat'] and form.cleaned_data['location_lng'])

        if request.method == 'POST' :
            form.save()

    return render(request, 'mainsite/add-settings.html', context)
