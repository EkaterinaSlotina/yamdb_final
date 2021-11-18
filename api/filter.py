from django_filters import rest_framework as filters

from .models import Title


class CustomFilter(filters.FilterSet):
    genre = filters.filters.CharFilter(field_name='genre__slug', )
    category = filters.filters.CharFilter(field_name='category__slug', )
    year = filters.filters.NumberFilter(field_name='year')
    name = filters.filters.CharFilter(field_name='name',
                                      lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ['genre', 'category', 'year', 'name']
