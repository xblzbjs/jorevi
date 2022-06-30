from django_filters import rest_framework as filters
from django_filters.filters import CharFilter, NumericRangeFilter

from jorevi.jobs.models import Job


class JobFilter(filters.FilterSet):

    type = CharFilter(field_name="type")
    category = CharFilter(field_name="category__name")
    company = CharFilter(field_name="company__name")
    salary = NumericRangeFilter(field_name="salary", lookup_expr="contained_by")

    class Meta:
        model = Job
        fields = ("type", "category", "company", "salary")
