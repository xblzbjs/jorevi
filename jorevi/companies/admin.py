from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from import_export.admin import ExportActionModelAdmin
from sorl.thumbnail.admin import AdminImageMixin
from tinymce.widgets import TinyMCE

from jorevi.companies.models import Company
from jorevi.companies.resources import CompanyExportResource
from jorevi.jobs.models import Job


class JobInline(admin.TabularInline):
    model = Job
    fields = (
        "title",
        "category",
        "type",
        "salary",
        "status",
        "creator",
    )
    classes = ("grp-collapse grp-open",)
    # status='published' should be first
    ordering = ["-status"]
    extra = 0


@admin.register(Company)
class CompanyAdmin(AdminImageMixin, ExportActionModelAdmin):
    list_display = (
        "logo_image",
        "name",
        "country",
        "website",
        "email",
        "phone",
        "logo",
        "is_verified",
    )
    list_filter = ("is_verified", "country")
    exclude = ("slug", "is_verified")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "logo",
                    ("name", "country", "website"),
                    ("email", "phone"),
                ),
            },
        ),
        (
            _("Overview"),
            {
                "fields": ("overview",),
            },
        ),
    )
    resource_class = CompanyExportResource
    search_fields = ("name", "email")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()

    @admin.display(description="Logo preview")
    def logo_image(self, obj):
        return mark_safe(  # nosec
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.logo.url,
                width=42,
                height=42,
            )
        )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "overview":
            return db_field.formfield(
                widget=TinyMCE(
                    mce_attrs={
                        "selector": "textarea",
                        "plugin": "textpattern",
                    },
                )
            )
        return super().formfield_for_dbfield(db_field, **kwargs)
