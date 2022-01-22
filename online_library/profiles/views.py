from django.shortcuts import render, redirect

from online_library.books.models import Book
from online_library.core.profile_utils import get_profile
from online_library.profiles.forms import EditProfileForm, DeleteProfileForm


def show_profile(request):
    profile = get_profile()
    context = {
        "profile": profile
    }
    return render(request, "profile.html", context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        form.save()
        return redirect("show profile")

    form = EditProfileForm(instance=profile)
    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, "edit-profile.html", context)


def delete_profile(request):
    profile = get_profile()
    books = Book.objects.all()
    if request.method == "POST":
        profile.delete()
        books.delete()
        return redirect("home")

    form = DeleteProfileForm(instance=profile)
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "delete-profile.html", context)
