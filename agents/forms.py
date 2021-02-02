from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import User

from .models import *


class AgentCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
        ]
