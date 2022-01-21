from django.urls import path

from notes.note.views import home, note_details, edit_note, delete_note, add_note

urlpatterns = [
    path("", home, name="home"),
    path("details/<int:pk>", note_details, name="note details"),
    path("add/", add_note, name="add note"),
    path("edit/<int:pk>", edit_note, name="edit note"),
    path("delete/<int:pk>", delete_note, name="delete note"),

]
