import django_filters

from .models import Event, EventError


class EventFilter(django_filters.FilterSet):
    session_id = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='timestamp', lookup_expr='gt', )
    end_date = django_filters.DateFilter(field_name='timestamp', lookup_expr='lt', )
    timestamp = django_filters.DateFilter(field_name='timestamp', lookup_expr='icontains', )

    class Meta:
        model = Event
        fields = ('session_id', 'category', 'name')


class EventErrorFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte', )
    end_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte', )

    class Meta:
        model = EventError
        fields = ()
