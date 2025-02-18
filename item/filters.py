from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Value
import django_filters
from .models import Item

class ItemFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_similarity')

    class Meta:
        model = Item
        fields = ['search']

    def filter_by_similarity(self, queryset, name, value):
        return queryset.annotate(
            similarity=TrigramSimilarity('item_name', value)
        ).filter(similarity__gt=0.2).order_by('-similarity')
