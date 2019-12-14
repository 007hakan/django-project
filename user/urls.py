from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("login/",views.loginUser,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.logoutUser,name="logout"),
]