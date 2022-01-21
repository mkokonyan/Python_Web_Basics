from django.shortcuts import render, redirect

from notes.note.models import Note
from notes.profiles.forms import ProfileForm
from notes.profiles.models import Profile


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = ProfileForm()
    context = {
        "form": form
    }
    return render(request, "home-no-profile.html", context)


def profile_details(request):
    profile = Profile.objects.first()
    notes = Note.objects.all().count()
    context = {
        "profile": profile,
        "notes": notes,
    }
    return render(request, "profile.html", context)


def delete_all(request):
    profile = Profile.objects.all()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect("home")
