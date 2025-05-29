
from django.urls import path
from .views import product_list, product_detail, category_list, category_detail
from .views import CustomUserListView, CustomUserDetailView



urlpatterns = [
    path("product_list/", product_list, name="product_list"),
    path("products/<slug:slug>/", product_detail, name="product-detail"),  
    path("category_list/", category_list, name="category-list"),
    path("category_detail/<slug:slug>/",
         category_detail, name="category-detail"),
   
]

