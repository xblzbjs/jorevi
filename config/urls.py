from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from filebrowser.sites import site
from rest_framework.authtoken.views import obtain_auth_token

admin.site.site_header = _("Jorevi Admin")
admin.site.site_title = _("Jorevi Admin")
admin.site.index_title = _("Welcome to jorevi")
admin.site.disable_action(_("delete_selected"))


urlpatterns = [
    path("users/", include("jorevi.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # TinyMCE
    path("tinymce/", include("tinymce.urls")),
    # Django Admin
    path(f"{settings.ADMIN_URL}filebrowser/", site.urls),
    path("grappelli/", include("grappelli.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    # Markdownx
    re_path(r"^markdownx/", include("markdownx.urls")),
    # API
    path("api/", include(("config.api_router", "api"), namespace="api"), name="api"),
    path("api/auth-token/", obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
