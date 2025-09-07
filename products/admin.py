from django.contrib import admin
from .models import Category
from .models import Products
# Register your models here.

# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Shows both name and parent in admin list
    prepopulated_fields = {'slug': ('name',)} 
    
admin.site.register(Products)