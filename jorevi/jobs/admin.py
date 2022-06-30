from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from import_export.admin import ExportActionMixin, ImportMixin
from import_export.formats import base_formats
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from jorevi.jobs.models import Category, Job
from jorevi.jobs.resources import CategoryResource, JobExportResource


@admin.register(Category)
class CategoryAdmin(ImportMixin, ExportActionMixin, DraggableMPTTAdmin):
    mptt_indent_field = "name"
    expand_tree_by_default = True
    mptt_level_indent = 50

    list_display = (
        "tree_actions",
        "indented_title",
        "related_jobs_count",
        "related_jobs_cumulative_count",
    )
    search_fields = ("name",)
    list_display_links = ("indented_title",)
    list_filter = (("parent", TreeRelatedFieldListFilter),)

    resource_class = CategoryResource

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative job count
        qs = Category.objects.add_related_count(
            qs, Job, "category", "jobs_cumulative_count", cumulative=True
        )

        # Add non cumulative job count
        qs = Category.objects.add_related_count(
            qs, Job, "category", "jobs_count", cumulative=False
        )

        return qs

    @admin.display(description=_("Related jobs (for this specific category)"))
    def related_jobs_count(self, instance):
        return instance.jobs_count

    @admin.display(description=_("Related jobs (in tree)"))
    def related_jobs_cumulative_count(self, instance):
        return instance.jobs_cumulative_count


@admin.register(Job)
class JobAdmin(ExportActionMixin, admin.ModelAdmin):
    autocomplete_fields = ("company", "category")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("title", "company", "category"),
                    ("type", "salary", "status"),
                ),
            },
        ),
        (
            _("Description"),
            {
                "classes": ("grp-collapse grp-opened",),
                "fields": ("redirect_url", "description"),
            },
        ),
    )
    list_display = (
        "title",
        "company",
        "category",
        "type",
        "salary",
        "show_redirect_url",
        "pub_date",
        "creator",
        "status",
        "created",
        "modified",
    )
    list_filter = ("company", "category", "type", "pub_date")
    resource_class = JobExportResource
    search_fields = ("title", "description", "company__name")
    actions = ("make_published", "make_finished")

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("company", "category", "creator")
        )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)

    @admin.display(description=_("Redirect url"))
    def show_redirect_url(self, obj):
        if obj.redirect_url:
            return format_html(
                "<a href='{url}'>detail</a>",
                url=obj.redirect_url,
            )
        return ""

    @admin.display(description=_("Mark selected jobs as published"))
    def make_published(self, request, queryset):
        queryset.update(status=Job.Status.PUBLISHED.value)
        queryset.update(pub_date=timezone.localdate())

    @admin.display(description=_("Mark selected jobs as finished"))
    def make_finished(self, request, queryset):
        queryset.update(status=Job.Status.FINISHED.value)

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLSX,
            base_formats.JSON,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]
