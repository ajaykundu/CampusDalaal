from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from productapp.models import ProductsModel


class CreateProduct(LoginRequiredMixin, generic.CreateView):
    fields = ("categoryid", "title",'prize','Description','productImage1','productImage2','productImage3','productImage4')
    model = ProductsModel
