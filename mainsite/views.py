from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

# Create your views here.
def login(request) :
    return render(request, 'registration/login.html')

@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id = request.user.id)
    return render(request, 'mainsite/top.html', {'user': user})
def signup(request) :
    return render(request, 'mainsite/signup.html')
