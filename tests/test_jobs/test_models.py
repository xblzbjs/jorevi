import pytest

from jorevi.jobs.models import Category, Job

from .factories import JobFactory

pytestmark = pytest.mark.django_db


class TestCategory:
    def test_str(self, category: Category):
        assert str(category) == f"{category.name}"

    def test_total_jobs(self, category: Category):
        JobFactory.create_batch(20, category=category)
        assert category.total_jobs() == Job.objects.filter(category=category).count()


class TestJob:
    def test_str(self, job: Job):
        assert str(job) == f"{job.title}"

    def test_salary_min(self, job: Job):
        if not job.salary:
            assert job.salary_min is None
        assert job.salary_min == job.salary.lower

    def test_salary_max(self, job: Job):
        if not job.salary:
            assert job.salary_max is None
        assert job.salary_max == job.salary.upper
