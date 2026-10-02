from django.contrib import admin
from django.urls import path, include

from store.views import (
    home,
    product_detail,
    add_to_cart,
    cart,
    remove_from_cart,
    increase_quantity,
    decrease_quantity,
    checkout,
    my_orders
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path(
        'product/<int:product_id>/',
        product_detail,
        name='product_detail'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path('cart/', cart, name='cart'),

    path(
        'remove-from-cart/<int:item_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'increase-quantity/<int:item_id>/',
        increase_quantity,
        name='increase_quantity'
    ),

    path(
        'decrease-quantity/<int:item_id>/',
        decrease_quantity,
        name='decrease_quantity'
    ),

    path('checkout/', checkout, name='checkout'),

    path('orders/', my_orders, name='my_orders'),

    path('users/', include('users.urls')),
]