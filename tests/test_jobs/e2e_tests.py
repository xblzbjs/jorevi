import json

import pytest
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from jorevi.jobs.models import Job

from ..test_companies.factories import CompanyFactory
from .factories import CategoryFactory, JobFactory

pytestmark = pytest.mark.django_db


User = get_user_model()


class TestJobEndpoints:

    endpoint = "/api/jobs/"

    def test_list(self, api_client):
        JobFactory.create_batch(30, status=Job.Status.PUBLISHED.value)
        # Common user
        common_user = User.objects.create_user(
            username="common user", email="common@user.com", password="common user"
        )
        token, _ = Token.objects.get_or_create(user=common_user)

        api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

        # Anonymous user
        api_client.credentials()

        response = api_client.get(self.endpoint)

        assert response.status_code == 401

    def test_retrieve(self, api_client):
        company = CompanyFactory()
        category = CategoryFactory()
        job = JobFactory(
            status=Job.Status.PUBLISHED.value, category=category, company=company
        )

        url = f"{self.endpoint}{job.uuid}/"
        # Common user
        common_user = User.objects.create_user(
            username="common user", email="common@user.com", password="common user"
        )
        token, _ = Token.objects.get_or_create(user=common_user)

        api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = api_client.get(url)

        assert response.status_code == 200

        # Anonymous user
        api_client.credentials()

        response = api_client.get(url)

        assert response.status_code == 401
