from online_library.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
