from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from backend_api.serializers import ServiceSerializer
from backend_api.models import Service
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
    serializer_class = ServiceSerializer

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


# def service_list(request):
#     query = request.GET.get("query", "")

#     services = Service.objects.filter(is_active=True)

#     if query:
#         services = services.filter(
#             Q(name__icontains=query) | Q(mini_description__icontains=query)
#         )

#     return render(
#         request,
#         "backend_api/service_list.html",
#         {
#             "services": services,
#             "query": query,
#         },
#     )


# def service_detail(request, pk):
#     service = get_object_or_404(Service, pk=pk)

#     context = {
#         "service": service,
#     }
#     return render(request, "backend_api/service_detail.html", context)


# def service_delete(request, pk):
#     service = get_object_or_404(Service, pk=pk)

#     if request.method == "POST":
#         service.is_active = False
#         service.save()

#         return redirect("service_list")

#     return redirect("service_list")
