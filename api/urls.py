
from django.urls import path
from .views import add_to_cart, product_list, product_detail, category_list, category_detail, update_cartitem_quantity, view_cart



urlpatterns = [
    path("product_list/", product_list, name="product_list"),
    path("products/<slug:slug>/", product_detail, name="product-detail"),  
    path("category_list/", category_list, name="category-list"),
    path("category_detail/<slug:slug>/", category_detail, name="category-detail"),

    path("add_to_cart/", add_to_cart, name="add-to-cart"),
    path("update_cartitem_quantity/" , update_cartitem_quantity, name="update-cartitem-quantity"),
    path("view_cart", view_cart, name="view-cart")
   
]

