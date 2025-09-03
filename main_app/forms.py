from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
class UserSignUpForm(UserCreationForm):
    icon = forms.ImageField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "icon"]