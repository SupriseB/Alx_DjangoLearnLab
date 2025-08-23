# blog/urls.py
from django.urls import path
from .views import BlogLoginView, BlogLogoutView, register, profile



# blog/urls.py

from django.urls import path
from .views import BlogLoginView, BlogLogoutView, register, profile
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/")
    path("posts/<int:post_id>/comments/new/', views.add_comment, name='add_comment"),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path("comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"),
    path('search/', views.blog_search, name='blog-search'),
    path('tags/<str:tag_name>/', views.blog_by_tag, name='blog-by-tag'),
    path("tags/<slug:tag_slug>/", "PostByTagListView.as_view()"),

]



