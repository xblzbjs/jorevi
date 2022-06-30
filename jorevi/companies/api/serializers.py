from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from jorevi.companies.models import Company


class CompanySerializer(CountryFieldMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = (
            "uuid",
            "url",
            "name",
            "website",
            "email",
            "phone",
            "overview",
            "country",
        )
        extra_kwargs = {
            "url": {"view_name": "api:company-detail", "lookup_field": "uuid"}
        }
