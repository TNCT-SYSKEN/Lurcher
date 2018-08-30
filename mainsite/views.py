from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets, serializers
from django_filters import rest_framework as filters
from mainsite.models import Account, Category, OfflineParty

import tweepy

# Create your views here.

def details(request, offline_party_id):
	party = OfflineParty.objects.get(id=offline_party_id)

	auth = tweepy.OAuthHandler('0nDoCPhIUgHeDtRXvMqnD6SaV', '9fTfhOSf87Atl8IBeCuRsuTJEBYCslF04fXA29aIfNmrGw2Za4')
	auth.set_access_token('952539721632071685-j04mmvU8ajsmv7KNh6kgrsB0q3EMybv', '7KhjYivQQDtcCtoXZljyByLAiQNxfMIGypV0lEGcMCEKO')
	api = tweepy.API(auth)

	sponsor_account = api.get_user(user_id=party.sponsor.twitter_id)
	sponsor_name = sponsor_account.name
	sponsor_screen_name = sponsor_account.screen_name
	sponsor_icon = sponsor_account.profile_image_url

	categories = party.category.all()

	participants = party.participant.all()
	participants_formatted = list()
	for participant in participants:
		participants_formatted.append((api.get_user(user_id=participant.twitter_id).screen_name, api.get_user(user_id=participant.twitter_id).profile_image_url))

	template = loader.get_template('mainsite/details.html')
	context = {
		'id': str(offline_party_id),
		'party': party,
		'categories': categories,
		'participants': participants_formatted,
		'sponsor_name': sponsor_name,
		'sponsor_screen_name': sponsor_screen_name,
		'sponsor_icon': sponsor_icon,
	}
	return HttpResponse(template.render(context, request))

def register(request, offline_party_id):
	# 〆鯖先輩の進捗を回収し次第ログイン絡みを実装する．
	party = OfflineParty.objects.get(id=offline_party_id)
	template = loader.get_template('mainsite/register.html')

	account = Account.objects.get(id=1)
	party.participant.add(account)

	context = {
		'party': party,
		'title': party.title,
	}
	return HttpResponse(template.render(context, request))

class CategoryFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr='contains')
    class Meta :
        model = Category
        fields = ['category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filter_class = CategoryFilter
