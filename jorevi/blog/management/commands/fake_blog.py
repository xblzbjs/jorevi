import random

from django.core.management.base import BaseCommand
from django.db import transaction
from factory.fuzzy import FuzzyChoice
from taggit.models import Tag, TaggedItem

from jorevi.blog.models import Category, Post
from jorevi.users.models import User
from tests.test_blog.factories import CategoryFactory, PostFactory


class Command(BaseCommand):
    help = "Generate blog test data"

    NUM_CATEGORIES = 10
    NUM_POSTS = 100
    TAGS_CHOICES = [
        "Bride",
        "Travel",
        "Python",
        "Go",
        "Django",
        "Web",
        "Flask",
        "Automation",
    ]

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Post, Category, Tag, TaggedItem]
        for m in models:
            m.objects.all().delete()
        self.stdout.write("Deleting successfully")

        self.stdout.write("Creating new categories...")
        categories = []
        for _ in range(self.NUM_CATEGORIES):
            category = CategoryFactory()
            categories.append(category)
        self.stdout.write("Create categories successfully...")

        self.stdout.write("Creating new posts...")
        for _ in range(self.NUM_POSTS):
            tag_list = self.TAGS_CHOICES
            random.shuffle(tag_list)
            tags = (tag for tag in tag_list[: random.randint(1, 5)])
            PostFactory(
                author=FuzzyChoice(User.objects.all()),
                category=FuzzyChoice(Category.objects.all()),
                tags=tags,
            )

        self.stdout.write("Create posts successfully...")
