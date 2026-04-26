from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories_per_100g', 'proteins', 'fats', 'carbs')
    search_fields = ('name',)

# Register your models here.
