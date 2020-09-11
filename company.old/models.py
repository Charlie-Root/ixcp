from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



COUNTRY_CHOICES = [
    ('NL', 'Netherlands'),
    ('BE', 'Belgium'),
]

class Company(models.Model):
    #company_user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=50)
    company_regid = models.CharField(max_length=5)
    company_vatid = models.CharField(max_length=5)
    company_street1 = models.CharField(max_length=50,null=True)
    company_street2 = models.CharField(max_length=50,null=True)
    company_zipcode = models.CharField(max_length=50,null=True)
    company_city = models.CharField(max_length=50,null=True)
    company_country = models.CharField(max_length=50,choices=COUNTRY_CHOICES,null=True)

    def __str__(self):
        return self.company_user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()