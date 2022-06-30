from django.db import models
from django.db.models.query import QuerySet


class CompanyQuerySet(QuerySet):
    """Custom queryset for company"""

    def get_verified(self):
        return self.filter(is_verified=True)


class CompanyManager(models.Manager):
    """Custom company manager"""

    def get_queryset(self):
        return CompanyQuerySet(self.model, using=self._db)

    def get_verified(self):
        return self.get_queryset().get_verified()
