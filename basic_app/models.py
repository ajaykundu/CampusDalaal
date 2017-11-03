from django.db import models
from django.contrib.auth.models import User

class IntitutionModel(models.Model):
    name = models.CharField(primary_key=True,max_length=512);
     #it will be show on object field.
    def __str__(self):
        return self.name

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
