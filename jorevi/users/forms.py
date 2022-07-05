from allauth.account.forms import (
    ChangePasswordForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    SignupForm,
)
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.urls import reverse
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "p-4 p-md-5 border rounded-3 bg-light"
        self.helper.form_action = reverse("account_login")
        self.helper.layout = Layout(
            Div(FloatingField("login"), css_class="form-floating mb-3"),
            Div(FloatingField("password"), css_class="form-floating mb-3"),
            Div(
                Div(Field("remember"), css_class="checkbok mb-0"),
                HTML(
                    """<a href="{% url 'account_reset_password' %}" class="text-body mb-3">Forgot password?</a>"""
                ),
                css_class="d-flex justify-content-between align-items-center",
            ),
            Submit("submit", "Sign in", css_class="w-100 btn btn-lg btn-primary"),
            HTML(
                """
                <p class="mt-3 mb-0">Not have an account?
                    <a href="{% url 'account_signup' %}">
                        Create an account
                    <i class='bx bx-chevrons-right bx-fade-right'></i>
                    </a>
                </p>
                <hr class="my-3">
                <h2 class="fs-5 fw-bold mb-3">Or use a third-party</h2>
                <button class="w-100 py-2 mb-2 btn btn-outline-dark rounded-3" type="submit">
                    <i class="bi-twitter"></i>
                    Sign in with Twitter
                </button>
                <button class="w-100 py-2 mb-2 btn btn-outline-primary rounded-3" type="submit">
                    <i class="bi-facebook"></i>
                    Sign in with Facebook
                </button>
                <button class="w-100 py-2 mb-2 btn btn-outline-secondary rounded-3" type="submit">
                    <svg class="bi me-1" width="16" height="16"><use xlink:href="#github"></use></svg>
                    <i class="bi-github"></i>
                    Sign in with Github
                </button>
                """
            ),
        )


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "p-4 p-md-5 border rounded-3 bg-light"
        self.helper.form_action = reverse("account_signup")
        self.helper.layout = Layout(
            Div(FloatingField("username"), css_class="form-floating mb-3"),
            Div(FloatingField("email"), css_class="form-floating mb-3"),
            Div(FloatingField("password1"), css_class="form-floating mb-3"),
            Div(FloatingField("password2"), css_class="form-floating mb-3"),
            Submit("submit", "Sign up", css_class="w-100 btn btn-lg btn-primary"),
            HTML(
                """
                <p class="mt-3 mb-0">Have an Account?
                    <a href="{% url 'account_login' %}">
                        Sign in
                    <i class='bx bx-chevrons-right bx-fade-right'></i>
                    </a>
                </p>
                <hr class="my-3">
                <h2 class="fs-5 fw-bold mb-3">Or use a third-party</h2>
                <button class="w-100 py-2 mb-2 btn btn-outline-dark rounded-3" type="submit">
                    <i class="bi-twitter"></i>
                    Sign up with Twitter
                </button>
                <button class="w-100 py-2 mb-2 btn btn-outline-primary rounded-3" type="submit">
                    <i class="bi-facebook"></i>
                    Sign up with Facebook
                </button>
                <button class="w-100 py-2 mb-2 btn btn-outline-secondary rounded-3" type="submit">
                    <svg class="bi me-1" width="16" height="16"><use xlink:href="#github"></use></svg>
                    <i class="bi-github"></i>
                    Sign up with Github
                </button>
                """
            ),
        )


class UserResetPasswordForm(ResetPasswordForm):
    """
    Form that will be rendered on a user reset password section/screen.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse("account_reset_password")
        self.helper.layout = Layout(
            Div(FloatingField("email"), css_class="form-floating mb-3"),
            Submit("submit", "Reset pasword", css_class="w-100 btn btn-lg btn-primary"),
        )


class UserChangePasswordForm(ChangePasswordForm):
    """
    Form that will be rendered on a user change password section/screen.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "p-4 p-md-5 border rounded-3 bg-light"
        self.helper.form_action = reverse("account_reset_password")
        self.helper.layout = Layout(
            Div(FloatingField("oldpassword"), css_class="form-floating mb-3"),
            Div(FloatingField("password1"), css_class="form-floating mb-3"),
            Div(FloatingField("password2"), css_class="form-floating mb-3"),
            Submit(
                "submit", "Change password", css_class="w-100 btn btn-lg btn-primary"
            ),
            HTML(
                """
                 <p>Please contact us if you have any trouble resetting your password.</p>
                """
            ),
        )


class UserResetPasswordKeyForm(ResetPasswordKeyForm):
    """
    Form that will be rendered on a user change password from key section/screen.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "p-4 p-md-5 border rounded-3 bg-light"
        # self.helper.form_action = reverse(".")
        self.helper.layout = Layout(
            Div(FloatingField("password1"), css_class="form-floating mb-3"),
            Div(FloatingField("password2"), css_class="form-floating mb-3"),
            Submit(
                "submit", "Change password", css_class="w-100 btn btn-lg btn-primary"
            ),
            HTML(
                """
                <hr class="my-3">
                <small>Please contact us if you have any trouble resetting your password.</small>
                """
            ),
        )
