import django_filters
from .models import Item
from Levenshtein import distance as levenshtein_distance

class ItemFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_distance')

    class Meta:
        model = Item
        fields = ['search']

    def filter_by_distance(self, queryset, name, value):
        results = []
        threshold = 4 # الحد الأقصى للاختلاف المسموح به (حسب الحاجة)

        for item in queryset:
            if levenshtein_distance(value.lower(), item.item_name.lower()) <= threshold:
                results.append(item.id)

        return queryset.filter(id__in=results)
