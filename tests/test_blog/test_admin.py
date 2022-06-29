import pytest
from django.urls import reverse

from tests.test_blog.factories import PostFactory

pytestmark = pytest.mark.django_db


class TestPostAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:blog_post_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:blog_post_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_view_post(self, admin_client):
        post = PostFactory()
        url = reverse("admin:blog_post_change", kwargs={"object_id": post.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
