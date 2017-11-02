from django.conf.urls import url

from . import views

app_name = 'productapp'

urlpatterns = [
    url(r"^$", views.ProductList.as_view(), name="all_products"),
    url(r"^newproduct/$",views.CreateProduct.as_view(), name="create"),
    url(r"^in/(?P<pk>\d+)/$",views.SingleProduct.as_view(),name="single"),
    # url(r'^api/get_drugs/',views.get_drugs, name='get_drugs'),
]
