from django.urls import path

from .views import *

app_name = 'agent'

urlpatterns = [
    path('agents/', AgentListView.as_view(), name='agent-list'),
    path('agent/create/', AgentCreateView.as_view(), name='agent-create'),
    path('agent/<username>/', AgentDetailView.as_view(), name='agent-detail'),
    path('agent/edit/<username>/', AgentUpdateView.as_view(), name='agent-update'),
    path('agent/delete/<username>/', AgentDeleteView.as_view(), name='agent-delete'),
]
