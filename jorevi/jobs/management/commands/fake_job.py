from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from factory.fuzzy import FuzzyChoice

from jorevi.companies.models import Company
from jorevi.jobs.models import Category
from tests.test_jobs.factories import JobFactory

app_models = apps.get_app_config("jobs").get_models()

User = get_user_model()


class Command(BaseCommand):
    help = "Set up job data"

    def add_arguments(self, parser):
        parser.add_argument(
            "total",
            nargs="+",
            type=int,
            help="Indicates the number of jobs to be created",
        )
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete old jobs data before creating",
        )

    @transaction.atomic
    def handle(self, *args, **options):

        total = options["total"][0]
        if options["delete"]:
            self.delete_old_data()
            self.create_category()

        self.stdout.write("Create new jobs...")
        for _ in range(total):
            JobFactory(
                company=FuzzyChoice(Company.objects.get_verified()),
                creator=FuzzyChoice(User.objects.all()),
            )
        self.stdout.write("Create jobs successfully")

        self.stdout.write("Finished!")

    def delete_old_data(self):
        self.stdout.write("Deleting old jobs data...")
        for model in app_models:
            model.objects.all().delete()
            self.stdout.write(f"Deleted {model.__name__} successfully!")
        self.stdout.write("Deleted successfully!")

    def create_category(self):
        self.stdout.write("Creating job categoryies...")
        self.create_root_nodes()
        self.create_child_nodes()
        self.stdout.write("Created job categories successfully")

    def create_root_nodes(self):
        Category.objects.create(name="Accounting and Consulting", parent=None)
        Category.objects.create(name="Admin Support", parent=None)
        Category.objects.create(name="Customer Service", parent=None),
        Category.objects.create(name="Data Science and Analysis", parent=None)
        Category.objects.create(name="Design and Creative", parent=None)
        Category.objects.create(name="Engineer and Architecture", parent=None),
        Category.objects.create(name="IT and Networking", parent=None)
        Category.objects.create(name="Legal", parent=None),
        Category.objects.create(name="Sales and Marketing", parent=None)
        Category.objects.create(name="Translation", parent=None)
        Category.objects.create(
            name="Web, Mobile and Software Development", parent=None
        )
        Category.objects.create(name="Writing", parent=None)

    def create_child_nodes(self):
        # Accounting and Consulting
        p1 = Category.objects.get(name="Accounting and Consulting")
        Category.objects.create(name="Accounting", parent=p1)
        Category.objects.create(name="Recruiting", parent=p1)
        # Admin Support
        p2 = Category.objects.get(name="Admin Support")
        Category.objects.create(name="Data Entry", parent=p2)
        Category.objects.create(name="Web & Software Product Research", parent=p2)
        # Customer Service
        p3 = Category.objects.get(name="Customer Service")
        Category.objects.create(name="Email, Phone & Chat Support", parent=p3)
        Category.objects.create(name="IT Support", parent=p3)
        # Data Science and Analysis
        p4 = Category.objects.get(name="Data Science and Analysis")
        Category.objects.create(name="Machine Learning", parent=p4)
        # Design and Creative
        p5 = Category.objects.get(name="Design and Creative")
        Category.objects.create(name="Audio Editing", parent=p5)
        # Engineer and Architecture
        p6 = Category.objects.get(name="Engineer and Architecture")
        Category.objects.create(name="CAD", parent=p6)
        # IT and Networking
        p7 = Category.objects.get(name="IT and Networking")
        Category.objects.create(name="DevOps Engineering", parent=p7)
        Category.objects.create(name="Cloud Engineering", parent=p7)
        # Legal
        p8 = Category.objects.get(name="Legal")
        Category.objects.create(name="Business & Corporate Law", parent=p8)
        # Sales and Marketing
        p9 = Category.objects.get(name="Sales and Marketing")
        Category.objects.create(name="Digital Marketing", parent=p9)
        # Translation
        p10 = Category.objects.get(name="Translation")
        Category.objects.create(name="Language Localization", parent=p10)
        # Web, Mobile and Software Development
        p11 = Category.objects.get(name="Web, Mobile and Software Development")
        Category.objects.create(name="Desktop Software Development", parent=p11)
        # Writing
        p12 = Category.objects.get(name="Writing")
        Category.objects.create(name="Content Writing", parent=p12)
