from django.conf.urls import url
from . import views
from .views import ProductViewSet
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'productapp'

from rest_framework import renderers

urlpatterns = [
    url(r"^$", views.ProductList.as_view(), name="all_products"),
    url(r"^updateProduct/(?P<pk>[\w-]+)/$",views.ProductUpdateView.as_view(),name="updateProduct"),
    url(r"^in/(?P<slug>[-\w]+)/$",views.SingleColgProduct.as_view(),name="singlecolg"),
    url(r"^newproduct/$",views.CreateProduct.as_view(), name="create"),
    url(r"^in/(?P<slug>[-\w]+)/in/(?P<pk>\d+)/$",views.SingleProduct.as_view(),name="single"),
    url(r'^autocomplete/$',views.AutoCompleteView.as_view(), name='autocomplete'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
