import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from slugify import slugify
from sorl.thumbnail import ImageField
from tinymce.models import HTMLField

from jorevi.companies.managers import CompanyManager


class Company(models.Model):
    """Company"""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(_("slug"), max_length=500)
    name = models.CharField(_("name"), max_length=255, unique=True)
    website = models.URLField(_("website"), max_length=255)
    email = models.EmailField(_("email"), null=True, unique=True)
    phone = PhoneNumberField(_("phone"), null=True, unique=True)
    overview = HTMLField(_("overview"), blank=True, null=True)
    logo = ImageField(_("logo"), upload_to="company/logos/")
    country = CountryField(null=True)

    is_verified = models.BooleanField(_("verfied status"), default=False)

    objects = CompanyManager()

    class Meta:
        db_table = "company"
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
