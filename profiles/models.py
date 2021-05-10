import uuid
import os
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


def profile_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/profile/{}/'.format(instance.user.username), filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    profile_pic = models.ImageField(null=True, upload_to=profile_image_file_path, default='default_profile_pic.png')

    profile_setup = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(id=self.id)
            if this.profile_pic != self.profile_pic:
                this.profile_pic.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile_user.save()
