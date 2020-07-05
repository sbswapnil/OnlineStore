from django.contrib import admin
from .models import Department, Product, ProductCatagory, Banner
from django import forms


# Register your models here.

admin.site.register(Department)
admin.site.register(Product)
admin.site.register(ProductCatagory)
admin.site.register(Banner)
