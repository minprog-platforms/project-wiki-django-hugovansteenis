from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.return_entry, name="entry"),
    path("search/", views.return_search, name="search"),
    path("new/", views.new_entry, name="new_entry"),
    path("edit/", views.edit_entry, name="edit_entry"),
    path("save_edit/", views.save_edit, name="save_edit"),
    path("random/", views.randomize, name="randomize")
]
