from django.shortcuts import render
from .models import Experience, Skill, Project, Technology


def index(request):
    skills = Skill.objects.all()
    technologies = Technology.objects.all()
    work_experience = Experience.objects.select_related('company').all()
    projects = Project.objects.all()
    template = 'main_page/index.html'

    context = {
        "skills": skills,
        "technologies": technologies,
        "work_experience": work_experience,
        "projets": projects,
    }
    return render(request, template, context)
