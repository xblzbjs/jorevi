import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CandidateManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Types.CANDIDATE)


class EmployerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Types.EMPLOYER)


class User(AbstractUser):
    """Default user for jorevi."""

    class Types(models.TextChoices):
        CANDIDATE = "CANDIDATE", _("Candidate")
        EMPLOYER = "EMPLOYER", _("Employer")

    base_type = Types.CANDIDATE

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("name of user"), blank=True, max_length=255)
    type = models.CharField(
        _("type"), max_length=50, choices=Types.choices, default=Types.CANDIDATE
    )
    email = models.EmailField(_("email address"), null=True, unique=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    phone_number = PhoneNumberField(
        verbose_name=_("phone number"),
        null=True,
        unique=True,
        help_text=_("Enter a valid phone number (e.g. +12125552368)."),
    )

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class Candidate(User):

    base_type = User.Types.CANDIDATE

    objects = CandidateManager()

    class Meta:
        proxy = True


class Employer(User):

    base_type = User.Types.EMPLOYER

    objects = EmployerManager()

    class Meta:
        proxy = True
