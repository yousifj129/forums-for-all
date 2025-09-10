from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view() , name="homepage"),
    path("auth/signup/", views.SignUpView.as_view() , name="signup"),
    path("forums/forums-list", views.ForumListView.as_view(), name="forums-list"),
    path("forums/forum-create", views.forum_create_view, name="forum-create"),

    path("forums/forum-details/<int:pk>", views.ForumDetailView.as_view(), name="forum-details"),
    path("forums/forum-delete/<int:pk>", views.ForumDeleteView.as_view(), name="forum-delete"),
    path("forums/forum-update/<int:pk>", views.ForumUpdateView.as_view(), name="forum-update"),

    path("forums/forum-upvote/<int:pk>", views.forum_upvote_view, name="forum-upvote"),
    path("forums/forum-downvote/<int:pk>", views.forum_downvote_view, name="forum-downvote"),
    path("forums/forum-comment/<int:pk>", views.forum_comment_view, name="forum-comment"),

    path("users/profile/<int:pk>", views.UserForumsListView.as_view(), name="user-profile"),
    path("forums/categories", views.CategoriesListView.as_view(), name="forum-categories"),

    
]
