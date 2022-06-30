from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from jorevi.companies.api.views import CompanyViewSet
from jorevi.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"users", UserViewSet, basename="user")
router.register(r"companies", CompanyViewSet, basename="company")

urlpatterns = router.urls
