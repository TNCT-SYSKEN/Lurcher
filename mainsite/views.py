from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from mainsite.models import OfflineParty

# Create your views here.

def details(request):
	party = OfflineParty.objects.get(id=2)
	categories = party.category.all()
	categories_str = ""
	for category in categories:
		categories_str += str(category) + " "

	participants = party.participant.all()
	participants_str = ""
	for participant in participants:
		participants_str += str(participant) + " "
		if len(participants_str) >= 15: #マジックナンバーをなんとかしたい
			break
	template = loader.get_template('mainsite/details.html')
	context = {
		'party': party,
		'categories': categories_str,
		'participants': participants_str
	}
	return HttpResponse(template.render(context, request))
