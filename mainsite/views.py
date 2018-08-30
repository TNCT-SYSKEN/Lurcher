from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mainsite.models import Account, OfflineParty, Category
from social_django.models import UserSocialAuth
from .forms import AccountForm

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
