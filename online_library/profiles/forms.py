from django import forms

from online_library.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = "disabled"
