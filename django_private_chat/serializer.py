from rest_framework import serializers
from django_private_chat.models import Dialog , Message
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','dialog','sender','text','created','modified')
