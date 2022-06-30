from rest_framework import serializers

from jorevi.jobs.models import Category, Job


class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("name", "parent", "children")

    def get_children(self, obj):
        return CategoryTreeSerializer(obj.get_children(), many=True).data


class JobSerializer(serializers.HyperlinkedModelSerializer):
    """Job list serializer class"""

    type = serializers.ReadOnlyField(source="get_type_display")
    category = serializers.ReadOnlyField(source="category.name")
    company_link = serializers.HyperlinkedRelatedField(
        source="company",
        many=False,
        read_only=True,
        view_name="api:company-detail",
        lookup_field="uuid",
    )
    company = serializers.ReadOnlyField(source="company.name")
    salary_min = serializers.ReadOnlyField()
    salary_max = serializers.ReadOnlyField()

    class Meta:
        model = Job
        fields = (
            "uuid",
            "url",
            "title",
            "description",
            "type",
            "category",
            "company",
            "company_link",
            "salary_min",
            "salary_max",
            "pub_date",
        )
        read_only_fields = (
            "type",
            "category",
            "company",
            "company_link",
            "salary_min",
            "salary_max",
        )
        extra_kwargs = {"url": {"view_name": "api:job-detail", "lookup_field": "uuid"}}

    def to_representation(self, instance):
        """
        add link relations in `links`
        """
        data = super().to_representation(instance)
        company_link = data.pop("company_link")
        self_link = data.pop("url")
        data["links"] = {"self": self_link, "company": company_link}
        return data
