from django.shortcuts import render
from .models import Experience, Skill, Project, Instrument


def index(request):
    skills = Skill.objects.all()
    instuments = Instrument.objects.all()
    current_job = Experience.objects.select_related('company').last()
    experience = Experience.objects.select_related('company').all()
    projects = Project.objects.all()
    template = 'main_page/index.html'

    context = {
        "skills": skills,
        "technologies": instuments,
        "current_job": current_job,
        "experience": experience,
        "projects": projects,
    }
    return render(request, template, context)
