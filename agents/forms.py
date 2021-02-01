from django import forms

from .models import *


class AgentCreateForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['user']
