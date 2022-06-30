from django.core.management.base import BaseCommand
from django.db import transaction

from jorevi.companies.models import Company
from tests.test_companies.factories import CompanyFactory


class Command(BaseCommand):
    help = "Set up company data"

    def add_arguments(self, parser):
        parser.add_argument(
            "total",
            nargs="+",
            type=int,
            help="Indicates the number of companies to be created",
        )
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete old companies data before creating",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        total = options.get("total")[0]
        if options["delete"]:
            self.delete_old_data()

        self.stdout.write("Creating new companies...")
        for _ in range(total):
            CompanyFactory()
        self.stdout.write("Created successfully!")

    def delete_old_data(self):
        self.stdout.write("Deleting old companies data...")
        models = [Company]
        for m in models:
            m.objects.all().delete()
        self.stdout.write("Deleted successfully!")
