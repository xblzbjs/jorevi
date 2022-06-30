from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from jorevi.companies.api.serializers import CompanySerializer
from jorevi.companies.models import Company


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "uuid"
    permission_classes = [IsAuthenticated]
    filterset_fields = ("country",)
    search_fields = ("name", "overview", "website", "email")
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return super().get_queryset().get_verified()
