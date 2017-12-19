from django.conf.urls import url
from . import views
app_name = 'productapp'

urlpatterns = [
    url(r"^$", views.ProductList.as_view(), name="all_products"),
    # url(r'^profilepage',views.List_product_for_profile.as_view(),name='profilepage'),
    url(r"^profilepageupdate/(?P<pk>[\w-]+)$",views.ProductUpdateView.as_view(),name="profilepageupdate"),
    url(r"^in/(?P<slug>[-\w]+)/$",views.SingleColgProduct.as_view(),name="singlecolg"),
    url(r"^newproduct/$",views.CreateProduct.as_view(), name="create"),
    url(r"^in/(?P<slug>[-\w]+)/in/(?P<pk>\d+)/$",views.SingleProduct.as_view(),name="single"),
    url(r'^autocomplete/$',views.AutoCompleteView.as_view(), name='autocomplete'),
]
