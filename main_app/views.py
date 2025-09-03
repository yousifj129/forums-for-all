from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserSignUpForm
class SignUpView(FormView):
    template_name = "registration/signup.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")  # or your home
