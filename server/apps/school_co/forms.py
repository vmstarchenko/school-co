from django import forms
from django.contrib.auth.forms import UserCreationForm

#registration forms - custom user registration
from server.apps.school_co.models import Teacher


class RegistrationFormTeacher(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='required')

    class Meta:
        model = Teacher
        fields = ("full_name", "school", "password", "confirm")

#TODO the same for pupil