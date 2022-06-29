import pytest

from jorevi.blog.models import Category, Post

pytestmark = pytest.mark.django_db


def test_post_str(post: Post):
    assert post.__str__() == f"{post.title}"


def test_category_str(category: Category):
    assert category.__str__() == f"{category.name}"
