# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account
from django import forms


class SignupageForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        exclude = ["user"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        exclude = ["user"]
