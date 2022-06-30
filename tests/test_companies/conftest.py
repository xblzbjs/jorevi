import pytest

from jorevi.companies.models import Company

from .factories import CompanyFactory


@pytest.fixture
def company() -> Company:
    return CompanyFactory()
