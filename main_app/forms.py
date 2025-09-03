from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import modelformset_factory

from .models import User, Forum,Attachment
class UserSignUpForm(UserCreationForm):
    icon = forms.ImageField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "icon"]

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ["title", "content"]
        # https://www.geeksforgeeks.org/python/django-form-field-custom-widgets/
        widgets = {
            "content": forms.Textarea()
        }