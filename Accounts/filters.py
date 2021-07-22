import django_filters
from .models import *
from django_filters import DateFilter
class OrderFilter(django_filters.FilterSet):
                           #model fiels                  #gete,lte
    start_date=DateFilter(field_name="added",lookup_expr='gte')
    end_date=DateFilter(field_name="added",lookup_expr='lte')
    class Meta:
        model=Order
        fields='__all__'
        exclude=['customer','added']