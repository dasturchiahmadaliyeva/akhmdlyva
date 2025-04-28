from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='static/')  # Internetdagi rasm uchun

    def __str__(self):
        return self.name
class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="social_links")
    platform = models.CharField(max_length=50)  # Masalan: GitHub
    url = models.URLField()

    def __str__(self):
        return f"{self.platform}: {self.url}"
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=100,)  # Masalan: React, Django
    project_link = models.URLField(null=True , blank=True)

    def __str__(self):
        return self.title

# Create your models here.
