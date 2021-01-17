# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    #Para cuando resetean lacontrasenia poradminlosmande allogin de usuarios
    path('accounts/login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    #path("logout/", LogoutView.as_view(), name="logout")
    path("accounts/logout/", views.logout, name="logout")

]
