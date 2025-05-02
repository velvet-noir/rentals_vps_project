from rest_framework import serializers
from backend_api.models import (
    Application,
    ApplicationService,
    ApplicationStatus,
    Service,
    ServiceSpecification,
)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["pk", "name", "image", "mini_description", "price"]


class ServiceSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSpecification
        fields = [
            "pk",
            "service",
            "description",
            "processor",
            "ram",
            "disk",
            "internet_speed",
        ]


class ServiceDetailSerializer(serializers.ModelSerializer):
    specifications = ServiceSpecSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ["pk", "name", "image", "mini_description", "price", "specifications"]


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ["pk", "name"]


# class ApplicationSerializer(serializers.ModelSerializer):
#     status = ApplicationStatusSerializer(read_only=True)

#     class Meta:
#         model = Application
#         fields = [
#             "pk",
#             "status",
#             "created_at",
#             "update_at",
#             "user_creator",
#             "user_moderator",
#         ]


class ApplicationSerializer(serializers.ModelSerializer):
    status = ApplicationStatusSerializer(read_only=True)
    services = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = [
            "pk",
            "status",
            "created_at",
            "update_at",
            "user_creator",
            "user_moderator",
            "services",
        ]

    def get_services(self, obj):
        services = Service.objects.filter(applications__application=obj)
        return ServiceSerializer(services, many=True).data


class ApplicationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationService
        fields = ["pk", "application", "service"]
