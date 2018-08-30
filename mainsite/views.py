from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from rest_framework import viewsets, serializers
from django_filters import rest_framework as filters

from .models import Account, OfflineParty, Category
from .forms import AccountForm, PageCreateForm

import tweepy

# Create your views here.

def add(request):#オフ会作成ページ
    form = PageCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request,'mainsite/form_success.html')
    #最初にこちらを通って、次にif文の中を通ります
    context = {
        'form': form
    }
    return render(request,'mainsite/ofukai_create.html',context)

def home(request):
    #指定ファイルの名前は調整してください
    return render(request,'ofukai_create.html')

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
    form = AccountForm(request.POST or None, initial={"twitter_id":user.access_token["user_id"]})
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