from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from reversion.admin import VersionAdmin
from sorl.thumbnail.admin import AdminImageMixin

from jorevi.blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(VersionAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(AdminImageMixin, VersionAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("image",),
                    ("title", "slug", "author"),
                    ("status", "published_date"),
                ),
            },
        ),
        (
            _("Category and Tags"),
            {
                "classes": ("grp-collapse grp-opened",),
                "fields": (("category", "tags"),),
            },
        ),
        (
            _("Description and Content"),
            {
                "classes": ("grp-collapse grp-closed",),
                "fields": ("description", "content"),
            },
        ),
    )

    list_per_page = 30
    list_display = (
        "title",
        "description",
        "category",
        "tag_list",
        "author",
        "status",
        "published_date",
        "created",
        "modified",
    )
    list_filter = ("created", "category", "status", "published_date")
    raw_id_fields = ("tags",)
    search_fields = ("title", "description")
    readonly_fields = (
        "slug",
        "published_date",
        "status",
        "author",
    )
    actions = ["make_published"]

    def get_queryset(self, request):
        return (
            super().get_queryset(request).prefetch_related("author", "category", "tags")
        )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    @admin.display(description=_("Mark selected posts as published"))
    def make_published(self, request, queryset):
        queryset.update(status="published")
        queryset.update(published_date=timezone.localdate())
