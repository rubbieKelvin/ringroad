from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.user import User
from .models.store import Store


@receiver(post_save, sender=User)
def create_store_on_user_create(
    sender: type[User], instance: User, created: bool, **kwargs
):
    if created:
        if instance.is_superuser:
            return

        store = Store.objects.create(
            name=f"{instance.full_name}'s store",
            description="My first store",
            owner=instance,
        )

        instance.last_accessed_store = store # type: ignore
        instance.save()
