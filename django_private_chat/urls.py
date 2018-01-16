# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
app_name = 'django_private_chat'

from rest_framework import renderers


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
]
