from django.contrib import admin
from .models import product
# Register your models here.

@admin.register(product)   # After creating this ProductAdmin class, register it with the admin site for the Product model
class ProductAdmin(admin.ModelAdmin):


    """ we are using this because we want to customize the admin interface for the product model,
    or to show how we want in admin panel"""

    list_display = ['name', 'sku', 'current_stock', 'selling_price']
    search_fields = ['name', 'sku']
    list_filter = ['created_at']