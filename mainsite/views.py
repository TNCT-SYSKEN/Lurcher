from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from mainsite.models import OfflineParty
from mainsite.models import Account

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
	party = OfflineParty.objects.get(id=offline_party_id)
	template = loader.get_template('mainsite/register.html')

	account = Account.objects.get(id=4)
	party.participant.add(account)

	auth = tweepy.OAuthHandler('0nDoCPhIUgHeDtRXvMqnD6SaV', '9fTfhOSf87Atl8IBeCuRsuTJEBYCslF04fXA29aIfNmrGw2Za4')
	auth.set_access_token('952539721632071685-j04mmvU8ajsmv7KNh6kgrsB0q3EMybv', '7KhjYivQQDtcCtoXZljyByLAiQNxfMIGypV0lEGcMCEKO')
	api = tweepy.API(auth)

	# 登録されている各アカウントについて，カテゴリ・Twitter での FF 関係をチェック．
	for a in Account.objects.all():
		isCategoryMatch = False
		if account.twitter_id == a.twitter_id: continue
		for c in account.category.all():
			if c in a.category.all():
				isCategoryMatch = True
				break
				

		if isCategoryMatch:
			friendship = api.show_friendship(source_id=account.twitter_id, target_id=a.twitter_id)[0]
			if friendship.following and friendship.followed_by:
				# カテゴリ・Twitter での FF が両方達成されていれば DM を送る．認証部分ができ次第ここを書き改めます
				print("FF " + api.get_user(user_id=a.twitter_id).screen_name + " " + api.get_user(user_id=account.twitter_id).screen_name)


	context = {
		'party': party,
		'title': party.title,
	}
	return HttpResponse(template.render(context, request))
