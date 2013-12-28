#coding=utf-8
from coltrane.models import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Category, CategoryAdmin)
