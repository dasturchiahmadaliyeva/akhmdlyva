from django.contrib import admin
from .models import Profile, SocialLink, Project,About
admin.site.register(Profile)
admin.site.register(SocialLink)
admin.site.register(Project)
admin.site.register(About)
# Register your models here.
