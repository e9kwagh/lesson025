from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("user_api/", views.start_api, name="api_response"),
    path("create/", views.create_obj, name="create_obj "),
    path("api/objects/<int:object_id>/update/", views.update_obj, name="update_object"),
    path("api/objects/<int:object_id>/delete/", views.delete_obj, name="delete_object"),
]
