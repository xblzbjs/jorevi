import random

from factory.faker import faker
from psycopg2.extras import NumericRange


def random_salary():
    min = random.randrange(10000, 1000000)
    max = random.randrange(min, min * 2)
    return NumericRange(
        min,
        max,
        bounds="[]",
    )


def random_multiple_countries(num: int = 3):

    FAKE = faker.Faker()
    countries = [FAKE.country_code(representation="alpha-2") for i in range(num)]
    return ",".join(countries)
