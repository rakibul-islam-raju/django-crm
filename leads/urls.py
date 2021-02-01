from django.urls import path

from .views import *

app_name = 'lead'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('edit/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
]
