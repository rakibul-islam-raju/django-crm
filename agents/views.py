import random

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from .models import *
from .forms import *
from .mixins import *


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agent/agent-list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agent/agent-create.html'
    form_class = AgentCreateForm
    success_url = reverse_lazy('agent:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(str(random.randint(0, 10000000)))
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            from_email='admin@djcrm.com',
            recipient_list=[user.email],
            subject='You are invited to be an agent.',
            message='You were created as an agent in DJCRM. Please login to start working.'
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'agent/agent-detail.html'
    context_object_name = 'agent'

    def get_object(self):
        organization = self.request.user.userprofile
        return get_object_or_404(
            Agent,
            organization=organization,
            user__username=self.kwargs.get('username')
        )


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agent/agent-update.html'
    context_object_name = 'agent'
    form_class = AgentCreateForm
    success_url = reverse_lazy('agent:agent-list')

    def get_object(self):
        return get_object_or_404(
            Agent,
            organization=organization,
            user__username=self.kwargs.get('username')
        )


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'delete.html'

    def get_object(self):
        return get_object_or_404(
            Agent,
            organization=organization,
            user__username=self.kwargs.get('username')
        )
