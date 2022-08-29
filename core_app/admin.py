from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin

from .models import Category, Color, Phone, PhoneImage


admin.site.register(Category)
admin.site.register(Color)


class ImageAdminInline(TabularInline):
    extra = 1
    model = PhoneImage


@admin.register(Phone)
class ProductModelAdmin(ModelAdmin):
    inlines = (ImageAdminInline, )

    fields = (
                'name', 'price', 'memory', 'color', 'description', 'category',
                'display', 'network_support', 'camera', 'computing_resources', 'battery',
                'secure_authentication', 'display_and_body', 'water_and_dust_protection',
                'audi_and_video', 'dimensions_and_weight', 'contents_of_delivery', 'photo'
              )

