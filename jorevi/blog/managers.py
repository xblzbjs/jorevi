from django.db import models
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet


class CategoryQuerySet(QuerySet):
    """Custom CategoryQuerySet for blog category"""

    def annotate_num_posts(self) -> QuerySet:
        return (
            self.filter(posts__status="published")
            .annotate(num_posts=Count("posts"))
            .values("name", "slug", "num_posts")
        )


class CategoryManager(models.Manager):
    """Custom Category Manager"""

    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def annotate_num_posts(self):
        return self.get_queryset().annotate_num_posts()


class PostQuerySet(QuerySet):
    """Custom PostQuerySet for blog post"""

    def get_published(self):
        return self.filter(status="published").order_by("-published_date")

    def get_draft(self):
        return self.filter(status="draft").all().order_by("modified")

    def get_by_category(self, category_name):
        return self.filter(category__name=category_name)

    def get_recent_posts(self, num=5):
        return self.get_published()[:num]


class PostManager(models.Manager):
    """Custom Post Manager"""

    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def get_by_category(self, category_name):
        return self.get_queryset().get_by_category(category_name)

    def get_published(self):
        return self.get_queryset().get_published()

    def get_draft(self):
        return self.get_queryset().get_draft()

    def get_recent_posts(self, num=5):
        return self.get_queryset().get_recent_posts(num)
