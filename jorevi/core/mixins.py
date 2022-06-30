class VerboseExportMixin:
    """Export with verbose name"""

    def get_export_headers(self):
        vnames = {
            i.name: i.verbose_name.capitalize()
            for i in self.Meta.model._meta.fields
            if i.verbose_name != "UUID"
        }
        return [vnames.get(i.split("__")[0], i) for i in super().get_export_headers()]
