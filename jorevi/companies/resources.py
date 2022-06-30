from import_export import resources

from jorevi.companies.models import Company
from jorevi.core.mixins import VerboseExportMixin


class CompanyExportResource(VerboseExportMixin, resources.ModelResource):
    class Meta:
        model = Company
        fields = (
            "name",
            "website",
            "email",
            "phone",
            "overview",
        )
        export_order = fields
        exclude = ("id",)
        import_id_fields = ("name",)
