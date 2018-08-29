from django.urls import path,include
from . import views
from django.contrib import admin
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), {'template_name': 'mainsite/login.html'}, name='login'),
    path('top/', views.top_page, name="top"),
    path('signup/', views.signup, name="signup"),
]
