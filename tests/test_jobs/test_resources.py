import pytest

from jorevi.jobs.resources import JobExportResource

from .factories import JobFactory

pytestmark = pytest.mark.django_db


class TestJobExportResource:
    @classmethod
    def setup_class(cls):
        cls.resource = JobExportResource()

    def test_fields(self):

        expected_fields = [
            "uuid",
            "title",
            "category",
            "company",
            "type",
            "description",
            "salary_min",
            "salary_max",
            "redirect_url",
        ]

        assert len(self.resource.fields) == len(expected_fields)

        assert all([e in self.resource.fields for e in expected_fields])

    def test_dehydrating_fields(self):
        job = JobFactory()
        salary_min = self.resource.export_field(self.resource.get_fields()[-3], job)
        salary_max = self.resource.export_field(self.resource.get_fields()[-2], job)

        assert salary_min == job.salary.lower
        assert salary_max == job.salary.upper

    def test_get_export_order(self):
        expected_headers = [
            "UUID",
            "Title",
            "Category",
            "Company",
            "Type",
            "Description",
            "Salary min",
            "Salary max",
            "Redirect url",
        ]
        assert self.resource.get_export_headers() == expected_headers
