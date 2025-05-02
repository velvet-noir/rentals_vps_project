from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from backend_api.serializers import (
    ApplicationSerializer,
    ServiceDetailSerializer,
    ServiceSerializer,
    ServiceSpecSerializer,
)
from backend_api.models import (
    Application,
    ApplicationStatus,
    Service,
    ServiceSpecification,
)
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class ServiceList(APIView):
    model_class = Service
    serializer_class = ServiceSerializer

    def get(self, request, format=None):
        query = request.query_params.get("query", None)
        services = self.model_class.objects.filter(is_active=True)

        if query:
            services = services.filter(
                Q(name__icontains=query) | Q(mini_description__icontains=query)
            )

        serializer = self.serializer_class(services, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetail(APIView):
    model_class = Service
    serializer_class = ServiceDetailSerializer

    def get(self, request, pk, format=None):
        service = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(service)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        service = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = get_object_or_404(self.model_class, pk=pk)
        service.is_active = False
        service.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceSpecList(APIView):
    model_class = ServiceSpecification
    serializer_class = ServiceSpecSerializer

    def get(self, request, format=None):
        services = self.model_class.objects.all()
        serializer = self.serializer_class(services, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceSpecDetail(APIView):
    model_class = ServiceSpecification
    serializer_class = ServiceSpecSerializer

    def get(self, request, pk, format=None):
        service = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(service)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        service = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = get_object_or_404(self.model_class, pk=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationList(APIView):
    model_class = Application
    serializer_class = ApplicationSerializer

    def get(self, request, format=None):
        services = self.model_class.objects.exclude(
            status__name__in=["draft", "deleted"]
        )

        serializer = self.serializer_class(services, many=True)
        return Response(serializer.data)


class ApplicationDetail(APIView):
    model_class = Application
    serializer_class = ApplicationSerializer

    def get(self, request, pk, format=None):
        application = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(application)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        application = get_object_or_404(self.model_class, pk=pk)

        formed_status = get_object_or_404(ApplicationStatus, pk=2)
        application.status = formed_status
        application.save()

        return Response(
            {"detail": "Заявка успешно сформирована."},
            status=status.HTTP_204_NO_CONTENT,
        )

    def delete(self, request, pk, format=None):
        application = get_object_or_404(self.model_class, pk=pk)

        deleted_status = get_object_or_404(ApplicationStatus, pk=5)
        application.status = deleted_status
        application.save()

        return Response(
            {"detail": "Заявка помечена как удалённая."},
            status=status.HTTP_204_NO_CONTENT,
        )
