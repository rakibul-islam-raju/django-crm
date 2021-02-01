from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
