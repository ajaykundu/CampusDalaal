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
from basic_app.models import UserProfileInfo,IntitutionModel
from django.core.exceptions import ObjectDoesNotExist
from braces.views import SelectRelatedMixin
from django.http import HttpResponse
import json


class SingleProduct(generic.DetailView):
    model = ProductsModel

class ProductList(generic.ListView):
    model = ProductsModel

    def get_queryset(self):
        if self.request.user.is_authenticated() :
            qs = super(ProductList, self).get_queryset()
            return qs.filter(Institution__exact=UserProfileInfo.objects.get(user=self.request.user).NameOfInstitute)
        else:
            return ProductsModel.objects.all()

class CreateProduct(LoginRequiredMixin, generic.CreateView):
    fields = ("categoryid","title",'prize','Description','productImage1','productImage2','productImage3','productImage4')
    model = ProductsModel


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.Institution = UserProfileInfo.objects.get(user=self.request.user).NameOfInstitute
        self.object.save()
        return super().form_valid(form)

class AutoCompleteView(generic.FormView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        Institutename = data.get('term', '')
        print(Institutename)
        users = IntitutionModel.objects.filter(name__icontains=Institutename)
        if Institutename :
            users = IntitutionModel.objects.filter(name__icontains=Institutename)
            print('maa ki chu')
            results = []
            for user in users:
                user_json = {}
                user_json['id'] = user.pk
                user_json['label'] = user.name
                user_json['value'] = user.name
                results.append(user_json)
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
