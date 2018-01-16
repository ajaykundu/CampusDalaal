from rest_framework import serializers
from productapp.models import ProductsModel ,ProductCategoryModel
from basic_app.models import IntitutionModel
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductsModel
        fields = ('id','user','Institution','categoryid','title', 'prize','Description',
                        'productImage1','productImage2','productImage3','productImage4','soldFlag','createdTime')

class ProductCategoryModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = ('url','typeOfProduct')
