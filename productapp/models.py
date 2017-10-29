from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from basic_app.models import IntitutionModel,UserProfileInfo

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# This is our category Table.
class ProductCategoryModel(models.Model):
    typeOfProduct = models.CharField(primary_key = True,max_length = 150)

    def __str__(self):
        return self.typeOfProduct

# this is out product model and related attributes to it.
class ProductsModel(models.Model):
    sellerid = models.ForeignKey(User,related_name = 'products',default = 'ajay')
    categoryid = models.ForeignKey(ProductCategoryModel, related_name = 'products')
    Institution = models.ForeignKey(IntitutionModel,related_name = 'products')

    #  i am not making title unique at here because i will make unique at
    # late point where sellerid,categoryid and title together will unique.
    title = models.CharField(max_length = 512)
    prize = models.DecimalField(max_digits=8, decimal_places=2)
    Description = models.TextField()
    productImage1 = models.ImageField(upload_to='photos/',blank = True)
    productImage2 = models.ImageField(upload_to = 'photos/',blank=True)
    productImage3 = models.ImageField(upload_to = 'photos/',blank=True)
    productImage4 = models.ImageField(upload_to = 'photos/',blank=True)
    # This flag is used to watch either the product is sold or not.
    soldFlag = models.BooleanField(default=False)
    #this field is added to get time when the product is uploaded.
    createdTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "UserproductPage:allpages",
            kwargs={
                "sellerid": self.user.username,
                "pk": self.pk
            }
        )


    class Meta:
        ordering = ["-createdTime"]
        unique_together = ["sellerid", "categoryid",'title']