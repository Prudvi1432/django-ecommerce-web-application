from django.contrib import admin

from .models import Product, CartItem, Order


# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'created_at',
    )

    search_fields = (
        'name',
        'description',
    )

    list_filter = (
        'created_at',
    )

    list_per_page = 20


# Cart Admin
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'product',
        'quantity',
    )

    search_fields = (
        'user__username',
        'product__name',
    )

    list_per_page = 20


# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'name',
        'email',
        'total_amount',
        'payment_method',
        'status',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
    )

    list_filter = (
        'status',
        'payment_method',
        'created_at',
    )

    list_per_page = 20