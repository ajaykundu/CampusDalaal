from rest_framework import serializers
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User


class UserProfileInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileInfo
        fields = ('user','NameOfInstitute')


class UserSerializer(serializers.ModelSerializer):
    user_info = UserProfileInfoSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','user_info')
