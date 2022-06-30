from django.core.management.base import BaseCommand
from django.db import transaction

from jorevi.users.models import User
from tests.test_users.factories import UserFactory


class Command(BaseCommand):
    help = "Set up users data"

    def add_arguments(self, parser):
        parser.add_argument(
            "total",
            nargs="+",
            type=int,
            help="Indicates the number of users to be created",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        total = options["total"][0]

        self.stdout.write("Deleting old user data...")
        # Don't delete superuser
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write("Creating new user data...")
        # Create all the users
        people = []
        for _ in range(total):
            person = UserFactory()
            people.append(person)
        self.stdout.write("Success")
