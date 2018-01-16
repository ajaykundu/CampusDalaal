from rest_framework import serializers
from django_private_chat.models import Dialog , Message
from django.contrib.auth.models import User


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url','id','dialog','sender','text','created','modified')

class DialogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dialog
        fields = ('url','owner','opponent')
