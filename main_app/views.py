from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, CreateView, ListView,DetailView, UpdateView
from .forms import UserSignUpForm, ForumForm
from .models import *
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")  # or your home

        
    

class HomePageView(TemplateView):
    template_name = "homepage.html"

class ForumListView(ListView):
    model = Forum
    template_name = "forums/forums-list.html"
    context_object_name = "forums"
    

    

class ForumDetailView(DetailView):
    model = Forum
    template_name = "forums/forum-details.html"
    context_object_name = "forum"
   
    
class ForumCreateView(CreateView):
    model = Forum
    template_name = "forums/forums-form.html"
    form_class = ForumForm

    # def get_form_kwargs(self):
    #     self.fields["creator"] = self.request.user.id

    #     return super().get_form_kwargs()
    

    def get_success_url(self):
        return reverse("forum-details", kwargs={"pk": self.object.pk})
    def form_valid(self, form):
    
        form.instance.creator = self.request.user.id
        print(form)
        return super().form_valid(form)
    
    