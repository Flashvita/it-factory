from django.db import models
from django.utils import timezone


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "workers"


class Shop(models.Model):
    title = models.CharField(max_length=255)
    worker = models.ForeignKey(
        "Worker",
        on_delete=models.CASCADE,
        related_name="worker_shops"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "shops"


class Visit(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    latitude = models.DecimalField(decimal_places=12, max_digits=15)
    longitude = models.DecimalField(decimal_places=12, max_digits=15)
    shop = models.ForeignKey(
        "Shop",
        on_delete=models.CASCADE,
        related_name="worker_visits"
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "visits"