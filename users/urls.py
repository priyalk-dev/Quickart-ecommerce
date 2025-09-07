# users/urls.py

from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("home", views.home, name="home"), 
    path('signup/', views.signup_view, name='signup'),  
    path('login/',views.user_login,name='login'),
    path('logout/', views.user_logout, name="logout"),
   
]
