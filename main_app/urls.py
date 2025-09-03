from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view() , name="homepage"),
    path("auth/signup/", views.SignUpView.as_view() , name="signup"),
    path("forums/forums-list", views.ForumListView.as_view(), name="forums-list"),
    path("forums/forum-create", views.forum_create_view, name="forum-create"),

    path("forums/forum-details/<int:pk>", views.ForumDetailView.as_view(), name="forum-details"),

]
