from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]