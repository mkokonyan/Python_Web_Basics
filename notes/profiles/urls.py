from django.urls import path

from notes.profiles.views import create_profile, profile_details, delete_all

urlpatterns = [
    path("", profile_details, name="profile details"),
    path("create/", create_profile, name="create profile"),
    path("delete_all/", delete_all, name="delete all"),
]
