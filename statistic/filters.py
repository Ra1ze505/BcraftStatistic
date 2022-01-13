from django_filters import rest_framework as filters
from .models import StaticItem


class ItemFilter(filters.FilterSet):
    start = filters.DateFilter(field_name="date", lookup_expr='gte', label='from')
    end = filters.DateFilter(field_name="date", lookup_expr='lte', label='to')

    class Meta:
        model = StaticItem
        fields = ['start', 'end']
