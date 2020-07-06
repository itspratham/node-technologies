from django.contrib import admin
from django.urls import path,include
from .views import login_view,homeview,logoutview,RegisterView
urlpatterns = [
    path('',RegisterView,name="register-view"),
    path('login/',login_view,name = "login-view"),
    path('home/',homeview,name="home-view"),
    path('logout/',logoutview,name= "log-out")
]
