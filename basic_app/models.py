from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class IntitutionModel(models.Model):
    name = models.CharField(primary_key=True,max_length=512)
    slug = models.SlugField(allow_unicode=True, unique=True)
     #it will be show on object field.
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("productapp:all_products", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]


# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)
    NameOfInstitute = models.ForeignKey(IntitutionModel)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
