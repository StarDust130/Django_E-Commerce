from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cart, CartItem, CustomUser , Products , Categories



# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    
admin.site.register(CustomUser, CustomUserAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', "featured")


admin.site.register( Products , ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register( Categories , CategoryAdmin)


admin.site.register([Cart , CartItem])