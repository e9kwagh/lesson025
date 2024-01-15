from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('',views.loginpage,name="loginpage"),
path('signupage',views.signupage,name = "signupage"),
path('home',views.home,name='home'),

]   
