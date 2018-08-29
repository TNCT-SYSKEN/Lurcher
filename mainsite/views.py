from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from mainsite.models import OfflineParty

# Create your views here.

def details(request):
	party = OfflineParty.objects.get(id=1)
	template = loader.get_template('mainsite/details.html')
	context = {
		'party': party,
	}
	return HttpResponse(template.render(context, request))
