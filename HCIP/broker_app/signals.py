from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

def create_user_profiles_for_existing_users():
    # Check if UserProfile model is available
    if hasattr(UserProfile, 'currency'):
        # Access UserProfile with currency
        # Your code to create user profiles here
        pass
    else:
        # Handle the situation where currency column is not available
        # Log a warning or provide default behavior
        print("Warning: UserProfile model does not have 'currency' column")

@receiver(post_migrate)
def post_migrate_handler(sender, **kwargs):
    create_user_profiles_for_existing_users()
