from django_filters import rest_framework as filters
from .models import Feedback

class FeedbackFilter(filters.FilterSet):
    section = filters.CharFilter(field_name='user__section', lookup_expr="iexact")
    batch = filters.CharFilter(field_name="user__year", lookup_expr="iexact")
    id_number = filters.CharFilter(field_name='user__username', lookup_expr='iexact')
    year = filters.NumberFilter(field_name='created__year')
    month = filters.NumberFilter(field_name='created__month')
    day = filters.NumberFilter(field_name='created__day')
    date = filters.DateFilter(field_name='created__date')
    start_date = filters.DateFilter(field_name="created", lookup_expr='gte')
    end_date = filters.DateFilter(field_name="created", lookup_expr='lte')

    class Meta:
        model = Feedback
        fields = '__all__'
