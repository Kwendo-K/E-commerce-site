from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "username"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            "<span class='form-text text-muted'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>"
        )

        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["placeholder"] = "firstname"
        self.fields["first_name"].label = ""
        self.fields["first_name"].help_text = (
            "<span class='form-text text-muted'><small></small></span>"
        )

        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["placeholder"] = "lastname"
        self.fields["last_name"].label = ""
        self.fields["last_name"].help_text = (
            "<span class='form-text text-muted'><small></small></span>"
        )

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "email"
        self.fields["email"].label = ""
        self.fields["email"].help_text = (
            "<span class='form-text text-muted'><small></small></span>"
        )

        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = "password"
        self.fields["password"].label = ""

        self.fields["confirm_password"].widget.attrs["class"] = "form-control"
        self.fields["confirm_password"].widget.attrs["placeholder"] = "confirm password"
        self.fields["confirm_password"].label = ""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["phone", "address"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["phone"].widget.attrs["class"] = "form-control"
        self.fields["phone"].widget.attrs["placeholder"] = "phone"
        self.fields["phone"].label = ""
        self.fields["phone"].help_text = (
            "<span class='form-text text-muted'><small>Required. Enter number without country code.</small></span>"
        )

        self.fields["address"].widget.attrs["class"] = "form-control"
        self.fields["address"].widget.attrs["placeholder"] = "address"
        self.fields["address"].label = ""
        self.fields["address"].help_text = (
            "<span class='form-text text-muted'><small></small></span>"
        )
