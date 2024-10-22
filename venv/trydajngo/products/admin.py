from django.contrib import admin

from .models import Product, DroneProduct

admin.site.register(Product)
admin.site.register(DroneProduct)

