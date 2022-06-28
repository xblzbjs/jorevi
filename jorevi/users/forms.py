from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "phone_number")
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
            "phone_number": {"unique": _("This phone has already been taken.")},
        }


class UserLoginForm(LoginForm):
    """
    Form that will be rendered on a user sign in section/screen.
    Default fields will be added automatically.
    """


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
