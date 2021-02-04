from django.db import models
from django.urls import reverse
from authentication.models import User, UserProfile
from agents.models import Agent


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)

    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('lead:lead-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('lead:lead-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('lead:lead-delete', kwargs={'pk': self.pk})
