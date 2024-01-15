from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('',views.loginpage,name="loginpage"),
path('signupage',views.signupage,name = "signupage"),
path('home',views.home,name='home'),
path("newcontact",views.create_contact, name="create_contact"),
path("updatecontact",views.update_contact, name="update_contact"),

]   
