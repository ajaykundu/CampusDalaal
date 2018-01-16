from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'


from rest_framework import renderers

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r"^updateinfo/(?P<pk>[\w-]+)/$",views.UpdateUserInfo.as_view(),name="updateinfo"),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^profilepage',views.List_product_for_profile.as_view(),name='profilepage'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
