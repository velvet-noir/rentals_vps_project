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


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ["pk", "name", "description"]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "pk",
            "status",
            "created_at",
            "update_at",
            "user_creator",
            "user_moderator",
        ]


class ApplicationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationService
        fields = ["pk", "application", "service"]
