from django.urls import path

from online_library.books.views import home, add_book, edit_book, show_book_details, delete_book

urlpatterns = [
    path("", home, name="home"),
    path("add/", add_book, name="add book"),
    path("edit/<int:pk>", edit_book, name="edit book"),
    path("delete/<int:pk>", delete_book, name="delete book"),
    path("details/<int:pk>", show_book_details, name="book details"),
]
