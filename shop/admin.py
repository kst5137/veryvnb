from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['c_name', 'c_slug']
    prepopulated_fields = {'c_slug': ('c_name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['writer', 'p_name', 'p_slug', 'category', 'price', 'stock', 'display', 'order', 'created', 'updated']
    list_filter = ['display', 'created', 'updated', 'category']
    prepopulated_fields = {'p_slug': ('p_name',)}
    list_editable = ['price', 'stock', 'display', 'order']
admin.site.register(Product, ProductAdmin)


def path_image_path(instance, filename):
    #{instance.content} => {instance.product.content}
    return f'products/{instance.product.content}/{filename}'


class ImageAdmin(admin.ModelAdmin):
    list_display = ['file']
admin.site.register(Image, ImageAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ['t_name']
admin.site.register(Type, TypeAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = ['z_name']
admin.site.register(Size, SizeAdmin)