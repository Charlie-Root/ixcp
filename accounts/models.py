from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

COUNTRY_CHOICES = [
    ('NL', 'Netherlands'),
    ('BE', 'Belgium'),
]


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=True)
    company_street = models.CharField(max_length=500, blank=True)
    company_houseno = models.CharField(max_length=500, blank=True)
    company_city = models.CharField(max_length=500, blank=True)
    company_country = models.CharField(max_length=50,choices=COUNTRY_CHOICES,null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()