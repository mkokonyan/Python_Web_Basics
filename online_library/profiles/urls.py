from django.urls import path

from online_library.profiles.views import show_profile, edit_profile, delete_profile

urlpatterns = [
    path("", show_profile, name="show profile"),
    path("edit/", edit_profile, name="edit profile"),
    path("delete/", delete_profile, name="delete profile"),
]
