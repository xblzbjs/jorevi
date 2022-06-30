import pytest

from jorevi.companies.models import Company

pytestmark = pytest.mark.django_db


class TestCompany:
    def test_str(self, company: Company):
        assert str(company) == f"{company.name}"
