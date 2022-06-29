import pytest

from jorevi.blog.models import Category, Post

from .factories import CategoryFactory, PostFactory


@pytest.fixture
def post() -> Post:
    return PostFactory()


@pytest.fixture
def category() -> Category:
    return CategoryFactory()
