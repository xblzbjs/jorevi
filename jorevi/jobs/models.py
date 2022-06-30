import uuid

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.postgres.fields import BigIntegerRangeField
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from slugify import slugify
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

from jorevi.companies.models import Company
from jorevi.jobs.managers import JobManager


class Category(MPTTModel):
    """Job category"""

    name = models.CharField(_("name"), max_length=200, unique=True)
    slug = models.SlugField(verbose_name=_("slug"), max_length=100)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        db_table = "job_category"
        order_insertion_by = ["name"]
        verbose_name = _("Job Category")
        verbose_name_plural = _("Job Categories")

    def __str__(self):
        return f"{self.name}"

    def total_jobs(self):
        return self.jobs.count()

    def get_absolute_url(self):
        return reverse("jobs:category", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Job(TimeStampedModel):
    """Worldwide remote job!!!"""

    class Type(models.TextChoices):
        PART_TIME = "pt", _("Part Time")
        FULL_TIME = "ft", _("Full Time")

    class Status(models.IntegerChoices):
        DRAFT = 0, _("Draft")
        FINISHED = 1, _("Finished")
        PUBLISHED = 2, _("Published")

    uuid = models.UUIDField("UUID", default=uuid.uuid4, editable=False)
    title = models.CharField(_("title"), max_length=250)
    description = HTMLField(_("description"))
    type = models.CharField(
        _("type"),
        max_length=2,
        choices=Type.choices,
        default=Type.FULL_TIME.label,
    )
    salary = BigIntegerRangeField(_("salary"), null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="jobs",
        verbose_name=_("category"),
        null=True,
    )
    tags = TaggableManager(verbose_name=_("tags"))
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs",
        verbose_name=_("company"),
    )
    redirect_url = models.URLField(verbose_name=_("redirect url"), null=True)
    status = models.PositiveSmallIntegerField(
        verbose_name=_("status"),
        choices=Status.choices,
        default=Status.DRAFT.label,
    )
    pub_date = models.DateTimeField(verbose_name=_("publish date"), editable=False)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="jobs",
        verbose_name=_("Creator"),
        null=True,
    )
    search_vector = SearchVectorField(null=True)

    objects = JobManager()

    class Meta:
        db_table = "job"
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")
        indexes = [
            GinIndex(fields=["search_vector"]),
        ]

    @property
    def company_name(self) -> str:
        """Company name"""
        return self.company.name

    @property
    def salary_min(self) -> int:
        """Job min salary"""
        return self.salary.lower if self.salary else None

    @property
    def salary_max(self) -> int:
        """Job max salary"""
        return self.salary.upper if self.salary else None

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        """Get url for job's detail view.

        Returns:
            str: URL for job detail
        """
        return reverse("jobs:detail", kwargs={"uuid": self.uuid})
