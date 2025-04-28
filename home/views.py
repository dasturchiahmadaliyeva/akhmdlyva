from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Profile, Project




class HomeView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'projects'