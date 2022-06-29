import random

import pytest
from pytest_django.asserts import assertQuerysetEqual

from jorevi.blog.managers import CategoryManager, PostManager
from jorevi.blog.models import Category, Post

from .factories import CategoryFactory, PostFactory

pytestmark = pytest.mark.django_db


class TestCategoryManager:
    category_manager = CategoryFactory._get_manager(Category)

    def test_get_queryset(self):
        assert self.category_manager == CategoryManager()
        assertQuerysetEqual(
            self.category_manager.get_queryset(), Category.objects.get_queryset()
        )

    def test_annotate_num_posts(self):
        assertQuerysetEqual(
            self.category_manager.annotate_num_posts(),
            Category.objects.annotate_num_posts(),
        )


class TestPostManager:
    post_manager = PostFactory._get_manager(Post)
    post_queryset = post_manager.get_queryset()

    def test_get_queryset(self):
        assert self.post_manager == PostManager()
        assertQuerysetEqual(self.post_queryset, Post.objects.get_queryset())

    def test_get_by_category(self):
        CategoryFactory.create_batch(8)
        PostFactory.create_batch(10)
        random_category_name = Category.objects.order_by("?").first().name
        assert isinstance(
            self.post_manager.get_by_category(random_category_name),
            type(Post.objects.get_by_category(random_category_name)),
        )

    def test_get_published(self):
        assertQuerysetEqual(
            self.post_manager.get_published(),
            Post.objects.get_published(),
        )

    def test_get_draft(self):
        assertQuerysetEqual(self.post_manager.get_draft(), Post.objects.get_draft())

    def test_get_published_recent_posts(self):
        num = random.randint(0, 10)
        assertQuerysetEqual(
            self.post_manager.get_recent_posts(num=num),
            Post.objects.get_published()[:num],
        )
