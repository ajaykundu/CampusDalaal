from rest_framework import serializers
from productapp.models import ProductsModel , ProductCategoryModel
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('categoryid','title', 'prize','Description',
                        'productImage1','productImage2','productImage3','productImage4')
