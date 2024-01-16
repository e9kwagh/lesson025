from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('',views.loginpage,name="loginpage"),
path('signupage',views.signupage,name = "signupage"),
path('home',views.home,name='home'),
path("newcontact",views.create_contact, name="create_contact"),
path("edit_contact/<int:contact_id>/",views.edit_contact, name="edit_contact"),
path("delete_contact/<int:contact_id>/", views.delete_contact, name="delete_contact"),
path('export_contacts/',views.export__to_csv, name='export__to_csv'),


]   
