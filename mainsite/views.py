from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets, serializers
from django_filters import rest_framework as filters
from mainsite.models import Category, OfflineParty

# Create your views here.

def details(request):
    party = OfflineParty.objects.get(id=1)
    template = loader.get_template('mainsite/details.html')
    context = {
        'party': party,
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
