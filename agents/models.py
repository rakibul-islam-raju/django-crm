from django.db import models
from django.urls import reverse
from authentication.models import User, UserProfile


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('agent:agent-detail', kwargs={'username': self.user.username})

    def get_update_url(self):
        return reverse('agent:agent-update', kwargs={'username': self.user.username})

    def get_delete_url(self):
        return reverse('agent:agent-delete', kwargs={'username': self.user.username})
    
    
