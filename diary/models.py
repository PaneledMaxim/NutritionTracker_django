from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    calories_per_100g = models.PositiveIntegerField()
    proteins = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    carbs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='created_products',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Create your models here.
