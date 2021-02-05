from django import forms

from .models import *


class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = [
            'agent',
            'date_added',
            'organization',
        ]


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
