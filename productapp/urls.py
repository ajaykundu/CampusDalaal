from django.conf.urls import url

from . import views

app_name = 'productapp'

urlpatterns = [
    url(r"^newproduct/$",views.CreateProduct.as_view(), name="create"),
]
