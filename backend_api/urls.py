from django.urls import path
from . import views

urlpatterns = [
    path("", views.service_list, name="service_list"),
    path("service/<int:pk>/", views.service_detail, name="service_detail"),
    path("service/<int:pk>/delete/", views.service_delete, name="service_delete"),
]
