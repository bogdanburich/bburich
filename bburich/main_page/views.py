from django.shortcuts import render
from .models import Experience, Skill, Project, Instrument


def index(request):
    skills = Skill.objects.all()
    instuments = Instrument.objects.all()
    work_experience = Experience.objects.select_related('company').all()
    projects = Project.objects.all()
    template = 'main_page/index.html'

    context = {
        "skills": skills,
        "technologies": instuments,
        "work_experience": work_experience,
        "projects": projects,
    }
    return render(request, template, context)
