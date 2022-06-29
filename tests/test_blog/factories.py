import factory
from django.utils import timezone
from factory import Faker
from factory.django import DjangoModelFactory, ImageField
from factory.faker import faker
from factory.fuzzy import FuzzyChoice

from jorevi.blog.models import Category, Post

from ..test_users.factories import UserFactory

fake = faker.Faker()

STATUS_CHOICES = [status[0] for status in Post.STATUS]


class CategoryFactory(DjangoModelFactory):

    name = Faker("sentence", nb_words=2)

    class Meta:
        model = Category
        django_get_or_create = ["name"]


class PostFactory(DjangoModelFactory):

    title = Faker("sentence", nb_words=5)
    description = Faker("text")
    author = factory.SubFactory(UserFactory)
    image = ImageField(width=1024, height=800, color="green")
    content = Faker("text", max_nb_chars=2000)
    category = factory.SubFactory(CategoryFactory)
    status = FuzzyChoice(STATUS_CHOICES)
    created = Faker("date_time", tzinfo=timezone.get_current_timezone())

    published_date = Faker("date_between", start_date=created)

    class Meta:
        model = Post

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # A list of tags were passed in, use them.
            for tag in extracted:
                self.tags.add(tag)
