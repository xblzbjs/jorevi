import pytest
from django.test.client import Client
from rest_framework.test import APIClient

from jorevi.users.models import User

from .test_users.factories import UserFactory


@pytest.fixture
def client() -> Client():
    return Client()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()
