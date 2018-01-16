from rest_framework import serializers
from basic_app.models import UserProfileInfo,IntitutionModel
from django.contrib.auth.models import User


class UserProfileInfoSerializer(serializers.HyperlinkedModelSerializer):
    NameOfInstitute = serializers.HyperlinkedRelatedField(many=False, view_name='intitutionmodel-detail', read_only=True)
    class Meta:
        model = UserProfileInfo
        fields = ('url','user','NameOfInstitute',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_info = UserProfileInfoSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = ('url','id','username','email','first_name','last_name','user_info')


class IntitutionModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntitutionModel
        fields = ('url','name',)
