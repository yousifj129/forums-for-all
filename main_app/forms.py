from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from .models import User, Forum,Attachment
class UserSignUpForm(UserCreationForm):
    icon = forms.ImageField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "icon"]

class ForumForm(forms.ModelForm):
    attachments = forms.ImageField()
    class Meta:
        model = Forum
        fields = ["title", "content", "attachments"]

    
