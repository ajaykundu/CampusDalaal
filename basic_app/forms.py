from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username','email','password1',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email addresses must be unique.')
        return email


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('NameOfInstitute',)
