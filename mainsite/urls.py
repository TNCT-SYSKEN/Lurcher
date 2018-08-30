from django.urls import path
from . import views

urlpatterns = [
	path('details/<int:offline_party_id>', views.details, name='details'),
	path('register/<int:offline_party_id>', views.register, name='register')
]
