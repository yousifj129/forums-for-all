from operator import itemgetter
from django.shortcuts import render,redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, CreateView, ListView,DetailView, UpdateView,DeleteView
from .forms import UserSignUpForm, ForumForm, CommentForm
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
    def get_queryset(self):
        queryset = super().get_queryset() # Get the default queryset

        search = self.request.GET.get("search")
        category = self.request.GET.get("category")
        if search:
            queryset = queryset.filter(content__icontains=search)
        if category:
            queryset = queryset.filter(category__icontains=category)
        

        return queryset

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super(ForumListView, self).get_context_data(**kwargs)
        unique_values = Forum.objects.values_list('category', flat=True).distinct()[:5]
        all_categories = []
        for value in unique_values:
            count = Forum.objects.filter(category=value).count()
            all_categories.append({
                "category":value,
                "count":count
            })
        newlist = sorted(all_categories, key=lambda d: d['count'], reverse=True)
        context["categories"] = newlist
        return context
    
class CategoriesListView(ListView):
    model = Forum
    template_name = "forums/forum-categories.html"
    context_object_name = "forums"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        unique_values = Forum.objects.values_list('category', flat=True).distinct()
        all_categories = []
        for value in unique_values:
            count = Forum.objects.filter(category=value).count()
            all_categories.append({
                "category":value,
                "count":count
            })
        newlist = sorted(all_categories, key=lambda d: d['count'], reverse=True)
        context["categories"] = newlist
        return context
    

        
    
    
        
    
    

    

class ForumDetailView(DetailView):
    model = Forum
    template_name = "forums/forum-details.html"
    context_object_name = "forum"
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class UserForumsListView(ListView):
    model = Forum
    template_name = "users/user-profile.html"
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["viewed_user"] = User.objects.get(pk=self.kwargs['pk'])
        context["forums"] = Forum.objects.filter(creator=self.kwargs['pk'])
        return context
    

class ForumDeleteView(DeleteView):
    model = Forum
    def get_success_url(self):
        return reverse("forums-list")    

class ForumUpdateView(UpdateView):
    model = Forum
    template_name = "forums/forum-update.html"
    form_class = ForumForm

    def get_success_url(self):
        return reverse("forum-details", kwargs={"pk": self.object.pk})

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
    
def forum_create_view(request):
    if request.method == "POST":
        form = ForumForm(request.POST)
        files = request.FILES.getlist("attachments")

        if form.is_valid():
            forum = form.save(commit=False)
            forum.creator = request.user
            forum.save()

            for f in files:
                Attachment.objects.create(
                    forum=forum,
                    file=f,
                    file_type="photo"  
                )

            return redirect("forums-list") 
    else:
        form = ForumForm()

    return render(request, "forums/forum-create.html", {"form": form})


def forum_upvote_view(request, pk):
    forum = Forum.objects.get(pk=pk)
    if request.method == "POST":
        try:
            Upvote.objects.create(forum=forum, user=request.user)
            try:
                Downvote.objects.get(forum=forum, user=request.user).delete()
            except:
                pass
        except:
            Upvote.objects.get(forum=forum, user=request.user).delete()


    return redirect(reverse('forum-details',kwargs={'pk':forum.pk}))

def forum_downvote_view(request, pk):
    forum = Forum.objects.get(pk=pk)
    if request.method == "POST":
        try:
            downvote = Downvote.objects.create(forum=forum, user=request.user)
            try:
                Upvote.objects.get(forum=forum, user=request.user).delete()
            except:
                pass
        except:
            Downvote.objects.get(forum=forum, user=request.user).delete()


    return redirect(reverse('forum-details',kwargs={'pk':forum.pk}))

def forum_comment_view(request, pk):
    if request.method == "POST":
        forum = Forum.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.forum = forum
            comment.save()
            return redirect(reverse('forum-details',kwargs={'pk':forum.pk}))
    else:
        form = CommentForm()
    return render(request, "forums/forum-create.html", {"form": form})
