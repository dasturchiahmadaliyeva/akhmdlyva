from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import Profile, Project, SocialLink, About


class HomeView(View):
    def get(self, request):
        projects = Project.objects.all()
        profile = Profile.objects.all().first()
        socia_lLink = SocialLink.objects.all()
        about = About.objects.first()

        context = {
            'projects': projects,
            'profile': profile,
            'social_links': socia_lLink,
            'about': about,
        }

        return render(request, 'home.html', context)
