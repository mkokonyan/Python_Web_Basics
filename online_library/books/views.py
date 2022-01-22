from django.shortcuts import render, redirect

from online_library.books.forms import AddBookForm, EditBookForm
from online_library.books.models import Book
from online_library.core.profile_utils import get_profile
from online_library.profiles.forms import CreateProfileForm


def home(request):
    profile = get_profile()

    if not profile:
        if request.method == "POST":
            form = CreateProfileForm(request.POST)
            form.save()
            return redirect("home")
    else:
        books = Book.objects.all()
        context = {
            "books": books,
            "profile": profile,
        }

        return render(request, "home-with-profile.html", context)

    form = CreateProfileForm()

    context = {
        "form": form,
    }
    return render(request, "home-no-profile.html", context)


def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        form.save()
        return redirect("home")

    profile = get_profile()
    form = AddBookForm()
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "add-book.html", context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("home")


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = EditBookForm(request.POST, instance=book)
        form.save()
        return redirect("home")

    profile = get_profile()
    form = AddBookForm(instance=book)
    context = {
        "profile": profile,
        "form": form,
        "book": book
    }
    return render(request, "edit-book.html", context)


def show_book_details(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()
    context = {
        "book": book,
        "profile": profile,
    }
    return render(request, "book-details.html", context)
