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



class ResourceIPv4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_prefix = models.CharField(max_length=500, blank=True)
    resource_country = models.CharField(max_length=50,choices=COUNTRY_CHOICES,null=True)
    resource_netname = models.CharField(max_length=500, blank=True)
    resource_description = models.CharField(max_length=500, blank=True)
    resource_organisation = models.CharField(max_length=500, blank=True)
    resource_admin_c = models.CharField(max_length=500, blank=True)
    resource_tech_c = models.CharField(max_length=500, blank=True)
    resource_mnt_lower = models.CharField(max_length=500, blank=True)
    resource_mnt_routes = models.CharField(max_length=500, blank=True)
    resource_mnt_domains = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ResourceIPv6(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_prefix = models.CharField(max_length=500, blank=True)
    resource_country = models.CharField(max_length=50,choices=COUNTRY_CHOICES,null=True)
    resource_netname = models.CharField(max_length=500, blank=True)
    resource_description = models.CharField(max_length=500, blank=True)
    resource_organisation = models.CharField(max_length=500, blank=True)
    resource_admin_c = models.CharField(max_length=500, blank=True)
    resource_tech_c = models.CharField(max_length=500, blank=True)
    resource_mnt_lower = models.CharField(max_length=500, blank=True)
    resource_mnt_routes = models.CharField(max_length=500, blank=True)
    resource_mnt_domains = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ResourceASN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=500, blank=True)
    resource_country = models.CharField(max_length=50,choices=COUNTRY_CHOICES,null=True)
    resource_organisation = models.CharField(max_length=500, blank=True)
    resource_website = models.CharField(max_length=500, blank=True)

class Peers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    peer_asn = models.ForeignKey(ResourceASN, on_delete=models.CASCADE)
    remote_asn = models.CharField(max_length=500, blank=True)
    peer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
