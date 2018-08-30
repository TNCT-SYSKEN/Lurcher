from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mainsite.models import Account, OfflineParty, Category
from social_django.models import UserSocialAuth
from rest_framework import viewsets, serializers
from django_filters import rest_framework as filters

from .models import Account, OfflineParty, Category
from .forms import AccountForm, PageCreateForm

import tweepy

# Create your views here.

def add(request):
    auth = tweepy.OAuthHandler('0nDoCPhIUgHeDtRXvMqnD6SaV', '9fTfhOSf87Atl8IBeCuRsuTJEBYCslF04fXA29aIfNmrGw2Za4')
    auth.set_access_token('952539721632071685-j04mmvU8ajsmv7KNh6kgrsB0q3EMybv', '7KhjYivQQDtcCtoXZljyByLAiQNxfMIGypV0lEGcMCEKO')
    api = tweepy.API(auth)

    account = Account.objects.get(id = request.user.id)
    form = PageCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form = form.save(commit = False)
        form.sponsor = account
        form.save()
        return render(request,'mainsite/create-success.html')

    context = {
        'form': form
    }
    return render(request,'mainsite/create.html',context)

def login(request) :
    return render(request, 'registration/login.html')

@login_required
def top_page(request):
    if Account.objects.filter(twitter_id = request.user.id).count() == 1:
        parties = OfflineParty.objects.all()
        user = UserSocialAuth.objects.get(user_id = request.user.id)
        template = loader.get_template('mainsite/top.html')
        context = {
            'parties': parties,
            'user': user,
        }
        return HttpResponse(template.render(context, request))
    else: # ここもうちょっとマシな実装したい
        return redirect('/signup/')
def signup(request) :
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    form = AccountForm(request.POST or None, initial={"twitter_id":user.access_token["user_id"], "access_token":user.access_token["oauth_token"], "access_token_secret":user.access_token["oauth_token_secret"]})
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request,'mainsite/top.html')

    category = list()
    for c in Category.objects.all():
        category.append(str(c))
    template = loader.get_template('mainsite/signup.html')
    context = {
        'form': form,
        'category': category,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

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

	account = Account.objects.get(id=request.user.id)
	party.participant.add(account)

	auth = tweepy.OAuthHandler('3wuvxJjBuBclWTxIHKtKx7I0H', 'PKeZeVXOqfGOmd5WRuDfIy059sga0xt9SmHa5WzZjOrtHFdWUX')
	auth.set_access_token(account.access_token.strip(), account.access_token_secret.strip())
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
				api.send_direct_message(user_id=str(a.twitter_id), text=str("「" + party.title + "」に申し込みました．あなたも参加してみませんか？ localhost:8000/details/" + str(party.id)))
				print("FF " + api.get_user(user_id=a.twitter_id).screen_name + " " + api.get_user(user_id=account.twitter_id).screen_name)


	context = {
		'party': party,
		'title': party.title,
	}
	return HttpResponse(template.render(context, request))

def list_page(request):
    parties = []
    categories = Account.objects.filter(id = request.user.id)[0].category.all()
    for c in categories :
        for p in OfflineParty.objects.all():
            for cat in p.category.all():
                if cat == c: parties.append(p)

    context = {
        "parties": parties
    }
    template = loader.get_template('mainsite/list.html')
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