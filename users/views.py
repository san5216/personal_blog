from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


class UserLoginView(LoginView):
    template_name = "users/login.html"



