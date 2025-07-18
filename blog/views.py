from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-date_posted"]
    template_name = "blog/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = "post_slug"
    template_name = "blog/post_detail.html"


class Dashboard(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-date_posted"]
    template_name = "blog/dashboard.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_update.html"
    slug_url_kwarg = "post_slug"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    slug_url_kwarg = "post_slug"

    def get_success_url(self):
        return reverse("blog:dashboard")


class PostSearchView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-date_posted"]
    template_name = "blog/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("query")
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return results
