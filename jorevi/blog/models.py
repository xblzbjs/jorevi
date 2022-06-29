import uuid

from django.conf import settings
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from slugify import slugify
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

from jorevi.blog.managers import CategoryManager, PostManager


class Category(models.Model):
    """Category of post"""

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=80)
    slug = models.SlugField(verbose_name=_("slug"), max_length=100)

    objects = CategoryManager()

    class Meta:
        db_table = "post_category"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(TimeStampedModel, models.Model):
    """Post of blog"""

    STATUS = Choices("draft", "published")
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)
    slug = models.SlugField(verbose_name=_("slug"), max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="posts",
        editable=False,
        null=True,
        verbose_name=_("author"),
    )
    image = ImageField(
        verbose_name=_("image"), upload_to="uploads/blog/posts/", null=True
    )
    content = HTMLField(_("content"))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("category"),
        null=True,
    )
    tags = TaggableManager(verbose_name=_("tags"))
    published_date = models.DateField(
        _("published date"), editable=False, null=True, blank=True
    )
    status = StatusField(_("status"))
    search_vector = SearchVectorField(null=True)

    objects = PostManager()

    class Meta:
        db_table = "post"
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        indexes = [
            GinIndex(fields=["search_vector"]),
        ]

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get url for post's detail view.

        Returns:
            str: URL for blog post detail
        """
        return reverse("blog:detail", kwargs={"slug": self.slug})
