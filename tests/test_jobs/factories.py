import factory
from django.contrib.auth import get_user_model
from django.utils import timezone
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from jorevi.jobs.models import Category, Job
from jorevi.utils.random import random_salary

from ..test_companies.factories import CompanyFactory
from ..test_users.factories import UserFactory

User = get_user_model()


class CategoryFactory(DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = Category
        django_get_or_create = ["name"]


class JobFactory(DjangoModelFactory):

    title = factory.Faker("job")
    category = factory.SubFactory(CategoryFactory)
    company = factory.SubFactory(CompanyFactory)
    type = FuzzyChoice(Job.Type.values)
    status = FuzzyChoice(Job.Status.values)
    description = factory.Faker("paragraph", nb_sentences=10)
    pub_date = factory.Faker(
        "date_time_between", start_date="-10d", tzinfo=timezone.get_current_timezone()
    )
    salary = factory.LazyFunction(random_salary)
    creator = factory.SubFactory(UserFactory)
    redirect_url = factory.Faker("url")

    class Meta:
        model = Job

    @factory.lazy_attribute
    def category(self):
        return Category.objects.order_by("?").first()
