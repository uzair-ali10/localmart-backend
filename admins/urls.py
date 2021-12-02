from django.urls import path
from .views import (
    create_and_get_products,
    create_and_get_properties,
    create_and_get_geometry,
    create_and_get_inventory,
    create_and_get_store,
    get_all_stores,
    get_inventory_products,
    make_payment
    )
urlpatterns = [
    path('product', create_and_get_products),
    path('prop', create_and_get_properties),
    path('geo', create_and_get_geometry),
    path('inventory', create_and_get_inventory),
    path('store', create_and_get_store),
    path('stores', get_all_stores),
    path('products/<int:pk>', get_inventory_products),
    path('payment', make_payment)
]