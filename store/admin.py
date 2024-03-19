from django.contrib import admin
from .models import Product, ProductVariant, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price_pounds',
        'category',
    )

    ordering = ('name', 'category', 'price_pounds')


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'type',
        'price_pounds',
    )

    ordering = ('product', 'type', 'price_pounds', 'name')


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'state',
        'price',
    )

    ordering = ('owner', 'state', 'price')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'product',
        'count',
        'price',
    )

    ordering = ('order', 'price')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
