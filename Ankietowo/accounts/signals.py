from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_users_group(sender, instance, created, **kwargs):
    if created:
        users_group = Group.objects.get(name='users')
        instance.groups.add(users_group)
