from django.urls import path
from . import views

app_name = 'lurcher'

urlpatterns = [
    path('offcreate',views.add, name='add'),
    path('home/',views.home, name='return_to_home')
    #home/でviewsの中のhomeという関数を呼び出し、
    #ホームのページに戻そうと思っているので調整をお願いします
]