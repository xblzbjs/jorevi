from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from jorevi.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"users", UserViewSet, basename="user")


urlpatterns = router.urls
