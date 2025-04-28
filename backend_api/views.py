from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import Service


def service_list(request):
    query = request.GET.get("query", "")

    services = Service.objects.filter(is_active=True)

    if query:
        services = services.filter(
            Q(name__icontains=query) | Q(mini_description__icontains=query)
        )

    return render(
        request,
        "backend_api/service_list.html",
        {
            "services": services,
            "query": query,
        },
    )


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)

    context = {
        "service": service,
    }
    return render(request, "backend_api/service_detail.html", context)


def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == 'POST':
        service.is_active = False
        service.save()

        return redirect('service_list')

    return redirect('service_list')