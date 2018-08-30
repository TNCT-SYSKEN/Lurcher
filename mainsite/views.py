from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mainsite.models import Account, OfflineParty
from social_django.models import UserSocialAuth

# Create your views here.
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
        user_id = request.user.id
        template = loader.get_template('mainsite/signup.html')
        context = {
            'user_id': user_id,
        }
        return HttpResponse(template.render(context, request))
def signup(request) : # 現在特に役割がない
    return render(request, 'mainsite/signup.html')
