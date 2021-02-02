from django.core.mail import send_mail
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from agents.mixins import OrganisorAndLoginRequiredMixin

from .forms import *
from .models import *


class LandingPageView(generic.TemplateView):
    template_name = 'landing-page.html'


class LeadCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    form_class = LeadCreateForm
    template_name = 'lead/lead-create.html'
    success_url = reverse_lazy('lead:lead-list')

    def form_valid(self, form):
        # TODO: send email
        return super(LeadCreateView, self).form_valid(form)


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lead/lead-list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(agent=user.agent)
        return queryset


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name='lead/lead-detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(agent=user.agent)
        return queryset


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name='lead/lead-update.html'
    form_class = LeadCreateForm
    context_object_name = 'lead'

    def get_queryset(self):
        return Lead.objects.filter(organization=self.request.user.userprofile)


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name='delete.html'
    success_url = reverse_lazy('lead:lead-list')

    def get_queryset(self):
        return Lead.objects.filter(organization=self.request.user.userprofile)
    