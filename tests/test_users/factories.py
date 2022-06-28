from typing import Any, Sequence

import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from factory import Faker, post_generation
from factory.fuzzy import FuzzyChoice

from jorevi.users.models import User


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):

    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")
    phone_number = Faker("phone_number")
    type = FuzzyChoice(User.Types.values)

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username", "email", "phone_number"]
