from django.urls import path
from . import views

urlpatterns = [
    path(r"services/", views.ServiceList.as_view(), name="services-list"),
    path(r"services/<int:pk>/", views.ServiceDetail.as_view(), name="services-detail"),
    path(r"services/spec", views.ServiceSpecList.as_view(), name="services-spec-list"),
    path(r"services/spec/<int:pk>/", views.ServiceSpecDetail.as_view(), name="services-spec-detail"),

    # path("", views.service_list, name="service_list"),
    # path("service/<int:pk>/", views.service_detail, name="service_detail"),
    # path("service/<int:pk>/delete/", views.service_delete, name="service_delete"),
]
