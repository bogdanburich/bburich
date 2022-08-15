from django.shortcuts import render

from .models import Experience, Instrument, Project, Skill


def index(request):
    skills = Skill.objects.all()
    instruments = Instrument.objects.all()
    current_job = (Experience.objects.select_related('company')
                   .latest('start_at'))
    experience = Experience.objects.select_related('company').all()
    projects = Project.objects.all()
    template = 'main_page/index.html'

    context = {
        "skills": skills,
        "instruments": instruments,
        "current_job": current_job,
        "experience": experience,
        "projects": projects,
    }
    return render(request, template, context)
