from django.contrib import admin
from productapp.models import  ProductCategoryModel,ProductsModel
# Register your models here.
admin.site.register(ProductCategoryModel)
admin.site.register(ProductsModel)
