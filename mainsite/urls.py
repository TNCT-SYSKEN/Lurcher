from django.urls import path,include
from rest_framework import routers
from . import views
from django.contrib import admin
import django.contrib.auth.views as auth_views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryList)

app_name = 'lurcher'

urlpatterns = [
    path('offcreate',views.add, name='add'),
    path('', auth_views.LoginView.as_view(), {'template_name': 'mainsite/login.html'}, name='login'),
    path('top/', views.top_page, name="top"),
    path('signup/', views.signup, name="signup"), # 叩かれることがない
    path('api/', include(router.urls)),
    path('details/<int:offline_party_id>', views.details, name='details'),
    path('register/<int:offline_party_id>', views.register, name='register'),
]
