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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_organisor:
            queryset = Lead.objects.filter(
                organization=self.request.user.userprofile,
                agent__isnull=True
            )
            context.update({
                'unassigned_list': queryset
            })
        return context


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


class LeadUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name='lead/lead-update.html'
    form_class = LeadCreateForm
    context_object_name = 'lead'

    def get_queryset(self):
        return Lead.objects.filter(organization=self.request.user.userprofile)


class LeadDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name='delete.html'
    success_url = reverse_lazy('lead:lead-list')

    def get_queryset(self):
        return Lead.objects.filter(organization=self.request.user.userprofile)


class AssignAgentView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = 'lead/agent-assign.html'
    form_class = AssignAgentForm
    success_url = reverse_lazy('lead:lead-list')

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lead/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
        
        context.update({
            'unassigned_lead_count': queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset


# class CategoryDetailView(LoginRequiredMixin, generic.ListView):
#     template_name = 'lead/categories.html'
#     queryset = Category.objects.all()
#     context_object_name = 'categories'
