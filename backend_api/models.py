from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    mini_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class ServiceSpecification(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="specifications"
    )
    description = models.TextField()
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    disk = models.CharField(max_length=100)
    internet_speed = models.CharField(max_length=100)

    def __str__(self):
        return self.service.name

    class Meta:
        ordering = ["id"]
        verbose_name = "Характеристика услуги"
        verbose_name_plural = "Характетистики услуг"
