from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import Creditss

@receiver(post_save, sender=Creditss)
def course_added(sender, instance, created, **kwargs):
    """
    This function will be called whenever a Credits instance is saved.
    """
    if created:
        # Your trigger logic here
        print(f"Course {instance.course} added. Execute trigger logic.")
