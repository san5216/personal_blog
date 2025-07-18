from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, Dashboard, PostSearchView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("post/new/", PostCreateView.as_view(), name="new"),
    path("post/results/", PostSearchView.as_view(), name="results"),
    path("post/<slug:post_slug>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<slug:post_slug>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<slug:post_slug>/delete/", PostDeleteView.as_view(), name="post_delete"),


]
