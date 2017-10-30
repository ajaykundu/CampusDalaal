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
from basic_app.models import UserProfileInfo

from braces.views import SelectRelatedMixin


class ProductList(generic.ListView):
    model = ProductsModel

class CreateProduct(LoginRequiredMixin, generic.CreateView):
    fields = ("categoryid","title",'prize','Description','productImage1','productImage2','productImage3','productImage4')
    model = ProductsModel


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.Institution = UserProfileInfo.objects.get(user=self.request.user).NameOfInstitute
        self.object.save()
        return super().form_valid(form)
