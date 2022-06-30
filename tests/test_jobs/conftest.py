import pytest

from jorevi.jobs.models import Category, Job

from .factories import CategoryFactory, JobFactory


@pytest.fixture
def category() -> Category:
    return CategoryFactory()


@pytest.fixture
def job() -> Job:
    return JobFactory()
