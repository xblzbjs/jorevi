from django.db import models
from django.db.models.query import QuerySet


class JobQuerySet(QuerySet):
    """Custom queryset for job"""

    def get_published(self):
        return self.filter(status=2).order_by("-pub_date")


class JobManager(models.Manager):
    """Custom job manager"""

    def get_queryset(self):
        return JobQuerySet(self.model, using=self._db)

    def get_published(self):
        return self.get_queryset().get_published()
