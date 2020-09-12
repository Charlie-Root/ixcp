from django.contrib import admin
from .models import Profile
from .models import ResourceIPv4
from .models import ResourceIPv6, ResourceASN, Peers

admin.site.register(Profile)
admin.site.register(ResourceIPv4)
admin.site.register(ResourceIPv6)
admin.site.register(ResourceASN)
admin.site.register(Peers)

# Register your models here.
