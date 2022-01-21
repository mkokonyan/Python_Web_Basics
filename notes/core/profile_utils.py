from notes.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if not profile:
        return None
    return profile
