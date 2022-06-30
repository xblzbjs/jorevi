from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import set_rollback


def custom_exception_handler(exc, context):

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied

    if isinstance(exc, exceptions.APIException):
        data = {
            "error": {
                "code": exc.status_code,
                "message": exc.default_detail,
                "detail": exc.get_full_details(),
            }
        }
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = f"{exc.wait}"

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None


class ExportError(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Export error")
    default_code = "export_error"


class ImportError(exceptions.APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _("Import error")
    default_code = "import_error"
