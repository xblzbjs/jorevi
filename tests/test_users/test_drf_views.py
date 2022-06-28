import pytest
from django.test import RequestFactory

from jorevi.users.api.views import UserViewSet
from jorevi.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)
        # TODO: Fix it
        response.data.pop("uuid")
        assert response.data == {
            # "uuid": user.uuid,
            "username": user.username,
            "name": user.name,
            "phone_number": user.phone_number,
            "email": user.email,
            # "profile": user.profile,
            "url": f"http://testserver/api/users/{user.username}/",
        }
