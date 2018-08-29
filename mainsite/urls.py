from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:party_id>', views.add_settings, name='add_settings')
]
