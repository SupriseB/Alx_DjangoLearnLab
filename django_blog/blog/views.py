from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import Q

from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, BlogForm, CommentForm
from .models import Blog as Post, Author, Comment
from taggit.models import Tag


# --------------------------
# Authentication Views
# --------------------------

class BlogLoginView(LoginView):
    template_name = 'registration/login.html'


class BlogLogoutView(LogoutView):
    template_name = 'registration/logout.html'


def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'account/profile.html', {'u_form': u_form, 'p_form': p_form})


# --------------------------
# Blog CRUD Views
# --------------------------

class BlogListView(ListView):
    model = Post
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"
    ordering = ["-published_date"]


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by("-created_at")
        context["comment_form"] = CommentForm()
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = BlogForm
    template_name = "blog/blog_form.html"

    def form_valid(self, form):
        author, created = Author.objects.get_or_create(user=self.request.user, defaults={
            "name": self.request.user.username
        })
        form.instance.author = author
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = BlogForm
    template_name = "blog/blog_form.html"

    def form_valid(self, form):
        form.instance.author = self.get_object().author
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog-list")

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author.user


# --------------------------
# Comment Views
# --------------------------

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        blog = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = blog
        form.instance.author = self.request.user
        messages.success(self.request, "Comment added successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog-detail", kwargs={"pk": self.kwargs["pk"]})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"

    def form_valid(self, form):
        messages.success(self.request, "Comment updated successfully!")
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse("blog-detail", kwargs={"pk": self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/delete_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse("blog-detail", kwargs={"pk": self.object.post.pk})


# --------------------------
# Tagging and Search Views
# --------------------------

def blog_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/blog_search.html', {'query': query, 'results': results})


def blog_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    blogs = Post.objects.filter(tags__in=[tag])
    return render(request, 'blog/blog_by_tag.html', {'tag': tag, 'blogs': blogs})
