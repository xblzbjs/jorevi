from django.utils.translation import gettext_lazy as _
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from jorevi.companies.models import Company
from jorevi.core.mixins import VerboseExportMixin
from jorevi.jobs.models import Category, Job


class CategoryResource(resources.ModelResource):

    parent = fields.Field(
        column_name="parent",
        attribute="parent",
        widget=ForeignKeyWidget(Category, "name"),
    )

    class Meta:
        model = Category
        skip_unchanged = True
        report_skipped = True
        exclude = ("id",)
        import_id_fields = ("name",)
        fields = ("parent", "name", "lft", "rght", "tree_id", "level")


class JobExportResource(VerboseExportMixin, resources.ModelResource):

    uuid = fields.Field(attribute="uuid", column_name="UUID")
    category = fields.Field(
        attribute="category",
        widget=ForeignKeyWidget(Category, field="name"),
        column_name=_("Category"),
    )
    company = fields.Field(
        attribute="company",
        widget=ForeignKeyWidget(Company, field="name"),
        column_name=_("Company"),
    )
    type = fields.Field(attribute="get_type_display", column_name=_("Type"))
    salary_min = fields.Field(column_name=_("Salary min"))
    salary_max = fields.Field(column_name=_("Salary max"))

    class Meta:
        model = Job
        fields = (
            "uuid",
            "title",
            "category",
            "company",
            "type",
            "description",
            "salary_min",
            "salary_max",
            "redirect_url",
        )
        export_order = fields
        exclude = ("id", "creator", "status")

    def dehydrate_salary_min(self, job) -> int:
        return job.salary_min

    def dehydrate_salary_max(self, job) -> int:
        return job.salary_max
