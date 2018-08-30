from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryList)

urlpatterns = [
	path('api/', include(router.urls)),
	path('details', views.details, name='details')
]
