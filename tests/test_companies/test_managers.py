import pytest
from pytest_django.asserts import assertQuerysetEqual

from jorevi.companies.managers import CompanyManager
from jorevi.companies.models import Company

from .factories import CompanyFactory

pytestmark = pytest.mark.django_db


class TestCompanyManager:
    company_manager = CompanyFactory._get_manager(Company)

    def test_get_queryset(self):
        assert self.company_manager == CompanyManager()
        assertQuerysetEqual(
            self.company_manager.get_queryset(), Company.objects.get_queryset()
        )

    def test_get_verified(self):
        assertQuerysetEqual(
            self.company_manager.get_verified(),
            Company.objects.get_verified(),
        )
