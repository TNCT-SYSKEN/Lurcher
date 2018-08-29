from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from mainsite.models import OfflineParty
import tweepy

# Create your views here.

def details(request):
	party = OfflineParty.objects.get(id=2)

	auth = tweepy.OAuthHandler('Consumer Token', 'Consumer Secret')
	auth.set_access_token('Access Token', 'Access Secret')
	api = tweepy.API(auth)

	sponsor_account = api.get_user(user_id=party.sponsor.twitter_id)
	sponsor_name = sponsor_account.screen_name
	sponsor_icon = sponsor_account.profile_image_url

	categories = party.category.all()
	categories_str = ""

	for category in categories:
		categories_str += str(category) + " "

	participants = party.participant.all()
	participants_str = ""
	for participant in participants:
		participants_str += api.get_user(user_id=participant.twitter_id).screen_name + " "

	template = loader.get_template('mainsite/details.html')
	context = {
		'party': party,
		'categories': categories_str,
		'participants': participants_str,
		'sponsor_name': sponsor_name,
		'sponsor_icon': sponsor_icon,
	}
	return HttpResponse(template.render(context, request))
