import pytest
from pytest_django.asserts import assertQuerysetEqual

from jorevi.users.models import (
    Candidate,
    CandidateManager,
    Employer,
    EmployerManager,
    User,
)

from .factories import UserFactory

pytestmark = pytest.mark.django_db


class TestCandidateManager:

    candidate_manager = UserFactory._get_manager(Candidate)

    def test_get_queryset(self):
        assert self.candidate_manager == CandidateManager()
        assertQuerysetEqual(
            self.candidate_manager.get_queryset(),
            User.objects.filter(type=User.Types.CANDIDATE),
        )


class TestEmployerManager:

    employer_manager = UserFactory._get_manager(Employer)

    def test_get_queryset(self):
        assert self.employer_manager == EmployerManager()
        assertQuerysetEqual(
            self.employer_manager.get_queryset(),
            User.objects.filter(type=User.Types.EMPLOYER),
        )
