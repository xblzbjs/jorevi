from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from jorevi.jobs.api.filters import JobFilter
from jorevi.jobs.api.serializers import CategoryTreeSerializer, JobSerializer
from jorevi.jobs.models import Category, Job


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = Category.objects.filter(level=0)
    serializer_class = CategoryTreeSerializer
    pagination_class = None
    filter_backends = []


class JobViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filterset_class = JobFilter
    lookup_field = "uuid"
    permission_classes = [IsAuthenticated]
    search_fields = ("title", "description", "company__name")
    throttle_classes = [UserRateThrottle]
    ordering_fields = ("type", "category__name", "pub_date")
    ordering = ["pub_date"]

    def get_queryset(self):
        return super().get_queryset().get_published()
