from django.contrib import admin

from tms.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Product)
class Productdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
