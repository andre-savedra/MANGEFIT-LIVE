from rest_framework import filters
import django_filters

from .models import *


class SaladaFilter(django_filters.FilterSet):
   categoria = django_filters.CharFilter(lookup_expr='icontains')
   nome = django_filters.CharFilter(lookup_expr='icontains')
   preco = django_filters.CharFilter(lookup_expr='lte')
   calorias = django_filters.CharFilter(lookup_expr='lte')

   class Meta:
      model = Salada
      fields = ['categoria','nome','preco', 'calorias']
