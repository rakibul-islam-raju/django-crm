from django import forms

from .models import *


class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = [
            'agent',
            'date_added'
        ]

