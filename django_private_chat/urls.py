# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
app_name = 'django_private_chat'

from rest_framework import renderers

message_list = views.MessageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
message_detail = views.MessageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



urlpatterns = [
    url(
        regex=r'^dialogs/(?P<username>[\w.@+-]+)$',
        view=views.DialogListView.as_view(),
        name='dialogs_detail'
    ),
    url(
        regex=r'^dialogs/$',
        view=views.DialogListView.as_view(),
        name='dialogs'
    ),
    url(r'^api/messages/$', message_list, name = 'message_list'),
    url(r'^api/messages/(?P<pk>[0-9]+)/$',message_detail,name='message_detail'),
]
