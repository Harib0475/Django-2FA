import django.forms as forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . import models


class SignUp(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
