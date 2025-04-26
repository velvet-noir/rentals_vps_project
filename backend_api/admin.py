from django.contrib import admin
from .models import Service, ServiceSpecification


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "price", "is_active")
    ordering = ("id",)

class ServiceSpecificationAdmin(admin.ModelAdmin):
    list_display = ("get_service_name", "processor", "ram", "disk", "internet_speed")
    ordering = ("id",)

    def get_service_name(self, obj):
        return f"Характеристика: {obj.service.name}"
    

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceSpecification, ServiceSpecificationAdmin)

