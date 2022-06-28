from django.utils.translation import gettext_lazy as _

from jorevi.users.apps import UsersConfig


class TestUsersConfig:
    def test_apps(self):
        assert UsersConfig.name == "jorevi.users"
        assert UsersConfig.verbose_name == _("Users")
