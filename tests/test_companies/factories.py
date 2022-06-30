from factory import Faker
from factory.django import DjangoModelFactory, ImageField
from factory.faker import faker

from jorevi.companies.models import Company

fake = faker.Faker()


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company
        database = "default"
        django_get_or_create = ["name", "email", "phone"]

    name = Faker("company")
    website = Faker("url")
    email = Faker("ascii_company_email")
    phone = Faker("phone_number")
    overview = Faker("text", max_nb_chars=3000)
    logo = ImageField(color="blue", width=100, height=100, format="JPEG")
    country = Faker("country_code", representation="alpha-2")
    is_verified = Faker("pybool")
