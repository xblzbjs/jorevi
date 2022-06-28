from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "jorevi.users"
    verbose_name = _("Users")

    def ready(self) -> None:
        import jorevi.users.signals  # noqa F401
