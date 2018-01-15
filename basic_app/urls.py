from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'


from rest_framework import renderers

user_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
userinfo_list = views.UserInfoViewSet.as_view({
        'get': 'list',
        'post': 'create'
})

userinfo_detail = views.UserInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r"^updateinfo/(?P<pk>[\w-]+)/$",views.UpdateUserInfo.as_view(),name="updateinfo"),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^profilepage',views.List_product_for_profile.as_view(),name='profilepage'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^api/user/$', user_list, name = 'user_list'),
    url(r'^api/user/(?P<pk>[0-9]+)/$',user_detail,name='user_detail'),
    url(r'^api/userinfo/$', userinfo_list, name = 'userinfo_list'),
    url(r'^api/userinfo/(?P<pk>[0-9]+)/$',userinfo_detail,name='userinfo_detail'),

]
